# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_45`
- **Frame Range:** 0 to 719 (720 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 719
- **Player Tracks:** 144
- **Ball Tracks:** 0
- **Action Segments:** 532
- **Validation Warnings:** 752
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 518
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `19` | `18` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `82` | `51` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `116` | `76` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `14` | `Group` | 0 | START | 2 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `15` | `Group` | 0 | START | 2 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `16` | `Group` | 0 | START | 7 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `18` | `Group` | 0 | START | 10 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `19` | `Group` | 0 | START | 11 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `19` | `18` | 16 | START | 16 | 49 |
| ✅ EXACT | `Action_KickBall` | Kicker | `19` | `18` | 108 | START | 108 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `82` | `51` | 272 | START | 272 | 325 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `116` | `76` | 680 | START | 680 | 706 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 11–156
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 15 | 5 | inferred_complete_timeline |
| `Action_KickApproach` | 16 | 49 | 34 | inferred_complete_timeline |
| `Action_KickApproach` | 52 | 71 | 20 | inferred_complete_timeline |
| `Action_KickApproach` | 86 | 94 | 9 | inferred_complete_timeline |
| `Action_KickApproach` | 96 | 107 | 12 | inferred_complete_timeline |
| `Action_KickBall` | 108 | 115 | 8 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_None` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 156 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 93 | 78 | inferred_complete_timeline |
| `Action_None` | 97 | 101 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 64 | 49 | inferred_complete_timeline |
| `Action_None` | 66 | 246 | 181 | inferred_complete_timeline |
| `Action_None` | 248 | 260 | 13 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 319 | 48 | inferred_complete_timeline |
| `Action_None` | 338 | 350 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 2–221
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_None` | 16 | 63 | 48 | inferred_complete_timeline |
| `Action_None` | 66 | 93 | 28 | inferred_complete_timeline |
| `Action_None` | 100 | 114 | 15 | inferred_complete_timeline |
| `Action_None` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_None` | 124 | 129 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_None` | 140 | 221 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 2–90
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_None` | 16 | 27 | 12 | inferred_complete_timeline |
| `Action_None` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_None` | 40 | 53 | 14 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 71 | 6 | inferred_complete_timeline |
| `Action_None` | 76 | 90 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 7–163
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 8 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 15 | 6 | inferred_complete_timeline |
| `Action_None` | 16 | 88 | 73 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 158 | 60 | inferred_complete_timeline |
| `Action_None` | 160 | 163 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 93 | 78 | inferred_complete_timeline |
| `Action_None` | 100 | 109 | 10 | inferred_complete_timeline |
| `Action_None` | 111 | 117 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 10–89
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 15 | 6 | inferred_complete_timeline |
| `Action_None` | 16 | 36 | 21 | inferred_complete_timeline |
| `Action_None` | 38 | 46 | 9 | inferred_complete_timeline |
| `Action_None` | 68 | 81 | 14 | inferred_complete_timeline |
| `Action_None` | 83 | 89 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 91 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Deep_Kick_Player1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 56 | 41 | inferred_complete_timeline |
| `Action_None` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 78 | 89 | 12 | inferred_complete_timeline |
| `Action_None` | 92 | 120 | 29 | inferred_complete_timeline |
| `Action_None` | 122 | 163 | 42 | inferred_complete_timeline |
| `Action_None` | 165 | 203 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Deep_Kick_Player2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 304 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 135 | 120 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 225 | 210 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 145 | 130 | inferred_complete_timeline |
| `Action_None` | 147 | 195 | 49 | inferred_complete_timeline |
| `Action_None` | 197 | 272 | 76 | inferred_complete_timeline |
| `Action_None` | 277 | 281 | 5 | inferred_complete_timeline |
| `Action_None` | 283 | 285 | 3 | inferred_complete_timeline |
| `Action_None` | 287 | 293 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–354
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 246 | 231 | inferred_complete_timeline |
| `Action_None` | 249 | 354 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 169 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 183 | 168 | inferred_complete_timeline |
| `Action_None` | 191 | 294 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–122 | 59 | 6 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–245 | 163 | 8 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 56–60 | 5 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 59–88 | 17 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 71–75 | 5 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 79–719 | 581 | 13 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 100–286 | 184 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 104–157 | 38 | 5 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 114–120 | 7 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 115–397 | 245 | 5 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 129–719 | 531 | 20 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 135–719 | 533 | 14 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 146–365 | 208 | 8 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 148–232 | 69 | 7 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 166–347 | 134 | 18 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 175–228 | 47 | 5 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 181–280 | 98 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 186–230 | 34 | 3 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 192–324 | 84 | 8 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 192–252 | 57 | 3 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 193–226 | 27 | 3 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 197–268 | 70 | 2 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 205–295 | 69 | 5 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `45` | `74` | Position_Unknown | Team_Unknown | 256–329 | 66 | 3 | Undefined position; Undefined team |
| `46` | `76` | Position_Unknown | Team_Unknown | 258–343 | 11 | 4 | Undefined position; Undefined team |
| `47` | `77` | Position_Unknown | Team_Unknown | 260–280 | 21 | 1 | Undefined position; Undefined team |
| `48` | `78` | Position_Unknown | Team_Unknown | 261–316 | 56 | 1 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 263–267 | 5 | 1 | Undefined position; Undefined team |
| `50` | `81` | Position_Unknown | Team_Unknown | 265–719 | 435 | 4 | Undefined position; Undefined team |
| `51` | `82` | Position_Unknown | Team_Unknown | 270–346 | 75 | 3 | Undefined position; Undefined team |
| `52` | `83` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `53` | `84` | Position_Unknown | Team_Unknown | 288–338 | 18 | 2 | Undefined position; Undefined team |
| `54` | `86` | Position_Unknown | Team_Unknown | 295–397 | 63 | 6 | Undefined position; Undefined team |
| `55` | `88` | Position_Unknown | Team_Unknown | 316–319 | 4 | 1 | Undefined position; Undefined team |
| `56` | `89` | Position_Unknown | Team_Unknown | 317–719 | 343 | 5 | Undefined position; Undefined team |
| `57` | `90` | Position_Unknown | Team_Unknown | 319–350 | 17 | 3 | Undefined position; Undefined team |
| `58` | `91` | Position_Unknown | Team_Unknown | 327–719 | 391 | 3 | Undefined position; Undefined team |
| `59` | `94` | Position_Unknown | Team_Unknown | 335–340 | 4 | 2 | Undefined position; Undefined team |
| `60` | `95` | Position_Unknown | Team_Unknown | 336–346 | 8 | 2 | Undefined position; Undefined team |
| `61` | `96` | Position_Unknown | Team_Unknown | 338–339 | 2 | 1 | Undefined position; Undefined team |
| `62` | `97` | Position_Unknown | Team_Unknown | 342–496 | 104 | 3 | Undefined position; Undefined team |
| `63` | `98` | Position_Unknown | Team_Unknown | 344–346 | 3 | 1 | Undefined position; Undefined team |
| `64` | `100` | Position_Unknown | Team_Unknown | 364–365 | 2 | 1 | Undefined position; Undefined team |
| `65` | `101` | Position_Unknown | Team_Unknown | 364–366 | 3 | 1 | Undefined position; Undefined team |
| `66` | `102` | Position_Unknown | Team_Unknown | 364–718 | 305 | 7 | Undefined position; Undefined team |
| `67` | `103` | Position_Unknown | Team_Unknown | 370–719 | 347 | 2 | Undefined position; Undefined team |
| `68` | `104` | Position_Unknown | Team_Unknown | 377–719 | 275 | 4 | Undefined position; Undefined team |
| `69` | `106` | Position_Unknown | Team_Unknown | 380–719 | 325 | 6 | Undefined position; Undefined team |
| `70` | `107` | Position_Unknown | Team_Unknown | 381–407 | 11 | 2 | Undefined position; Undefined team |
| `71` | `108` | Position_Unknown | Team_Unknown | 381–719 | 305 | 8 | Undefined position; Undefined team |
| `72` | `109` | Position_Unknown | Team_Unknown | 381–382 | 2 | 1 | Undefined position; Undefined team |
| `73` | `111` | Position_Unknown | Team_Unknown | 384–385 | 2 | 1 | Undefined position; Undefined team |
| `74` | `112` | Position_Unknown | Team_Unknown | 387–400 | 4 | 2 | Undefined position; Undefined team |
| `75` | `114` | Position_Unknown | Team_Unknown | 389–392 | 4 | 1 | Undefined position; Undefined team |
| `76` | `116` | Position_Unknown | Team_Unknown | 392–706 | 312 | 3 | Undefined position; Undefined team |
| `77` | `120` | Position_Unknown | Team_Unknown | 401–402 | 2 | 1 | Undefined position; Undefined team |
| `78` | `122` | Position_Unknown | Team_Unknown | 404–719 | 315 | 2 | Undefined position; Undefined team |
| `79` | `123` | Position_Unknown | Team_Unknown | 405–719 | 298 | 6 | Undefined position; Undefined team |
| `80` | `125` | Position_Unknown | Team_Unknown | 406–719 | 307 | 6 | Undefined position; Undefined team |
| `81` | `126` | Position_Unknown | Team_Unknown | 407–425 | 8 | 3 | Undefined position; Undefined team |
| `82` | `127` | Position_Unknown | Team_Unknown | 407–719 | 300 | 7 | Undefined position; Undefined team |
| `83` | `128` | Position_Unknown | Team_Unknown | 407–719 | 303 | 3 | Undefined position; Undefined team |
| `84` | `131` | Position_Unknown | Team_Unknown | 420–719 | 286 | 4 | Undefined position; Undefined team |
| `85` | `133` | Position_Unknown | Team_Unknown | 422–719 | 278 | 6 | Undefined position; Undefined team |
| `86` | `135` | Position_Unknown | Team_Unknown | 424–719 | 296 | 1 | Undefined position; Undefined team |
| `87` | `136` | Position_Unknown | Team_Unknown | 426–719 | 293 | 2 | Undefined position; Undefined team |
| `88` | `137` | Position_Unknown | Team_Unknown | 426–427 | 2 | 1 | Undefined position; Undefined team |
| `89` | `139` | Position_Unknown | Team_Unknown | 432–448 | 7 | 2 | Undefined position; Undefined team |
| `90` | `143` | Position_Unknown | Team_Unknown | 458–459 | 2 | 1 | Undefined position; Undefined team |
| `91` | `144` | Position_Unknown | Team_Unknown | 465–471 | 7 | 1 | Undefined position; Undefined team |
| `92` | `145` | Position_Unknown | Team_Unknown | 481–484 | 4 | 1 | Undefined position; Undefined team |
| `93` | `149` | Position_Unknown | Team_Unknown | 493–587 | 79 | 4 | Undefined position; Undefined team |
| `94` | `150` | Position_Unknown | Team_Unknown | 493–500 | 8 | 1 | Undefined position; Undefined team |
| `95` | `151` | Position_Unknown | Team_Unknown | 501–502 | 2 | 1 | Undefined position; Undefined team |
| `96` | `153` | Position_Unknown | Team_Unknown | 509–538 | 12 | 4 | Undefined position; Undefined team |
| `97` | `154` | Position_Unknown | Team_Unknown | 511–512 | 2 | 1 | Undefined position; Undefined team |
| `98` | `155` | Position_Unknown | Team_Unknown | 514–716 | 128 | 11 | Undefined position; Undefined team |
| `99` | `156` | Position_Unknown | Team_Unknown | 515–521 | 4 | 2 | Undefined position; Undefined team |
| `100` | `157` | Position_Unknown | Team_Unknown | 519–668 | 114 | 11 | Undefined position; Undefined team |
| `101` | `159` | Position_Unknown | Team_Unknown | 523–683 | 138 | 9 | Undefined position; Undefined team |
| `102` | `160` | Position_Unknown | Team_Unknown | 525–526 | 2 | 1 | Undefined position; Undefined team |
| `103` | `163` | Position_Unknown | Team_Unknown | 538–539 | 2 | 1 | Undefined position; Undefined team |
| `104` | `169` | Position_Unknown | Team_Unknown | 554–646 | 41 | 12 | Undefined position; Undefined team |
| `105` | `176` | Position_Unknown | Team_Unknown | 607–717 | 88 | 5 | Undefined position; Undefined team |
| `106` | `179` | Position_Unknown | Team_Unknown | 610–694 | 43 | 5 | Undefined position; Undefined team |
| `107` | `180` | Position_Unknown | Team_Unknown | 610–719 | 88 | 9 | Undefined position; Undefined team |
| `108` | `181` | Position_Unknown | Team_Unknown | 611–613 | 3 | 1 | Undefined position; Undefined team |
| `109` | `182` | Position_Unknown | Team_Unknown | 611–714 | 28 | 6 | Undefined position; Undefined team |
| `110` | `185` | Position_Unknown | Team_Unknown | 616–650 | 17 | 5 | Undefined position; Undefined team |
| `111` | `186` | Position_Unknown | Team_Unknown | 616–635 | 19 | 2 | Undefined position; Undefined team |
| `112` | `187` | Position_Unknown | Team_Unknown | 617–719 | 83 | 6 | Undefined position; Undefined team |
| `113` | `188` | Position_Unknown | Team_Unknown | 617–618 | 2 | 1 | Undefined position; Undefined team |
| `114` | `192` | Position_Unknown | Team_Unknown | 621–691 | 14 | 7 | Undefined position; Undefined team |
| `115` | `194` | Position_Unknown | Team_Unknown | 631–633 | 3 | 1 | Undefined position; Undefined team |
| `116` | `196` | Position_Unknown | Team_Unknown | 637–694 | 26 | 5 | Undefined position; Undefined team |
| `117` | `197` | Position_Unknown | Team_Unknown | 638–719 | 75 | 3 | Undefined position; Undefined team |
| `118` | `204` | Position_Unknown | Team_Unknown | 647–650 | 4 | 1 | Undefined position; Undefined team |
| `119` | `206` | Position_Unknown | Team_Unknown | 651–719 | 61 | 4 | Undefined position; Undefined team |
| `120` | `207` | Position_Unknown | Team_Unknown | 651–683 | 26 | 2 | Undefined position; Undefined team |
| `121` | `208` | Position_Unknown | Team_Unknown | 652–719 | 60 | 2 | Undefined position; Undefined team |
| `122` | `210` | Position_Unknown | Team_Unknown | 654–658 | 5 | 1 | Undefined position; Undefined team |
| `123` | `215` | Position_Unknown | Team_Unknown | 661–714 | 51 | 3 | Undefined position; Undefined team |
| `124` | `216` | Position_Unknown | Team_Unknown | 661–671 | 10 | 2 | Undefined position; Undefined team |
| `125` | `218` | Position_Unknown | Team_Unknown | 665–714 | 21 | 5 | Undefined position; Undefined team |
| `126` | `219` | Position_Unknown | Team_Unknown | 666–698 | 26 | 3 | Undefined position; Undefined team |
| `127` | `220` | Position_Unknown | Team_Unknown | 666–698 | 9 | 2 | Undefined position; Undefined team |
| `128` | `221` | Position_Unknown | Team_Unknown | 672–719 | 42 | 4 | Undefined position; Undefined team |
| `129` | `222` | Position_Unknown | Team_Unknown | 675–677 | 3 | 1 | Undefined position; Undefined team |
| `130` | `224` | Position_Unknown | Team_Unknown | 677–707 | 13 | 3 | Undefined position; Undefined team |
| `131` | `225` | Position_Unknown | Team_Unknown | 679–719 | 40 | 2 | Undefined position; Undefined team |
| `132` | `226` | Position_Unknown | Team_Unknown | 681–685 | 5 | 1 | Undefined position; Undefined team |
| `133` | `228` | Position_Unknown | Team_Unknown | 690–701 | 12 | 1 | Undefined position; Undefined team |
| `134` | `231` | Position_Unknown | Team_Unknown | 695–714 | 12 | 2 | Undefined position; Undefined team |
| `135` | `233` | Position_Unknown | Team_Unknown | 702–719 | 11 | 3 | Undefined position; Undefined team |
| `136` | `235` | Position_Unknown | Team_Unknown | 707–715 | 7 | 2 | Undefined position; Undefined team |
| `137` | `236` | Position_Unknown | Team_Unknown | 708–719 | 12 | 1 | Undefined position; Undefined team |
| `138` | `237` | Position_Unknown | Team_Unknown | 708–714 | 7 | 1 | Undefined position; Undefined team |
| `139` | `238` | Position_Unknown | Team_Unknown | 709–719 | 9 | 2 | Undefined position; Undefined team |
| `140` | `242` | Position_Unknown | Team_Unknown | 713–714 | 2 | 1 | Undefined position; Undefined team |
| `141` | `243` | Position_Unknown | Team_Unknown | 713–719 | 7 | 1 | Undefined position; Undefined team |
| `142` | `244` | Position_Unknown | Team_Unknown | 715–719 | 5 | 1 | Undefined position; Undefined team |
| `143` | `245` | Position_Unknown | Team_Unknown | 717–719 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `82` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `Kicker` position mapped to `offense` team
- ⚠️ 127 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 127 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 254 |
| Missing visible bounding boxes during action | 496 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 719 as fallback play end.
- ⚠️ Action 'Action_None' range [16-93] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-354] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-135] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-89] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-163] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-203] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-304] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-183] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-294] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-195] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-293] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-64] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-246] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-260] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-319] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-350] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-93] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-109] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-109] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-165] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-178] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-114] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-36] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-90] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-88] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-158] for track '16' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-36] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [16-49] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [52-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [86-94] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [108-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-156] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-158] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-266] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-286] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-380] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-415] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-421] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-442] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-494] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-506] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-139] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-160] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-286] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-109] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-135] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-188] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-349] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-384] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-242] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-548] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-569] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-576] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-584] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-593] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-598] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-643] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-674] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-684] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-688] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-693] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [697-702] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [714-719] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-277] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-327] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-384] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-407] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-648] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-172] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-347] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-361] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-157] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-219] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-232] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-181] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-209] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-226] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-242] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-262] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-322] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-347] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-228] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-280] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-200] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-219] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-201] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-319] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-244] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-252] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-226] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-263] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-250] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-278] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-307] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-321] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-280] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-316] for track '48' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-347] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-365] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-385] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [272-325] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [328-346] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-338] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-324] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-355] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-382] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-382] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-387] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-719] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-343] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-672] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-690] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-496] for track '62' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-366] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-385] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-665] for track '66' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-677] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [694-695] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [712-718] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-637] for track '67' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-719] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-386] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-492] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-719] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-411] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-423] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-434] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-438] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-387] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-407] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-419] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-639] for track '71' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-673] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-703] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-710] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-392] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-470] for track '76' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-679] for track '76' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [680-706] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-546] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-502] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-670] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-676] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-701] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [704-709] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [714-719] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-422] for track '80' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-627] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-641] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-670] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-689] for track '80' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-417] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-411] for track '82' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-421] for track '82' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-444] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-468] for track '82' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-564] for track '82' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-719] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-411] for track '83' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-617] for track '83' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-719] for track '83' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-593] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-677] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [679-702] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-719] for track '84' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-665] for track '85' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-677] for track '85' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [679-681] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-704] for track '85' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-701] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-436] for track '89' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-471] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-484] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-559] for track '93' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-569] for track '93' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-500] for track '94' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-513] for track '96' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-538] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '97' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-523] for track '98' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-556] for track '98' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-600] for track '98' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-622] for track '98' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-631] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-639] for track '98' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-653] for track '98' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-659] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [668-669] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-690] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [715-716] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-516] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-524] for track '100' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-545] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-549] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-576] for track '100' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-589] for track '100' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-605] for track '100' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-621] for track '100' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-627] for track '100' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-637] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-652] for track '100' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [656-668] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-582] for track '101' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-594] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-597] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-625] for track '101' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-637] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-646] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-658] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [664-670] for track '101' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-683] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '102' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-559] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-564] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-580] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-616] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-623] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-633] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-637] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [643-646] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-618] for track '105' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-657] for track '105' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [660-683] for track '105' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-712] for track '105' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [714-717] for track '105' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-627] for track '106' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-635] for track '106' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-649] for track '106' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-667] for track '106' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-694] for track '106' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-617] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-627] for track '107' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-646] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-658] for track '107' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-667] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-678] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-681] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-702] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [704-719] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-613] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-617] for track '109' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-627] for track '109' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-635] for track '109' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-646] for track '109' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [679-680] for track '109' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [712-714] for track '109' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-621] for track '110' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-627] for track '110' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-641] for track '110' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-646] for track '110' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-650] for track '110' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-629] for track '111' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-635] for track '111' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-629] for track '112' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-635] for track '112' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [643-661] for track '112' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-667] for track '112' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-681] for track '112' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-618] for track '113' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-627] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-635] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-663] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-667] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-687] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-691] for track '114' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-633] for track '115' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-646] for track '116' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-650] for track '116' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-666] for track '116' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-691] for track '116' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-694] for track '116' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-650] for track '117' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [656-661] for track '117' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [664-719] for track '117' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-650] for track '118' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-684] for track '119' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-690] for track '119' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [696-714] for track '119' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-719] for track '119' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-654] for track '120' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-683] for track '120' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-668] for track '121' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-658] for track '122' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-674] for track '123' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-703] for track '123' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-714] for track '123' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-668] for track '124' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-671] for track '124' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-668] for track '125' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-671] for track '125' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-681] for track '125' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-687] for track '125' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-714] for track '125' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-667] for track '126' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-678] for track '126' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-698] for track '126' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-668] for track '127' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-698] for track '127' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-676] for track '128' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [679-683] for track '128' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-702] for track '128' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-677] for track '129' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-678] for track '130' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-695] for track '130' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-707] for track '130' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [679-680] for track '131' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-719] for track '131' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [681-685] for track '132' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-701] for track '133' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [695-698] for track '134' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [707-714] for track '134' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-704] for track '135' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-712] for track '135' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [715-719] for track '135' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [707-711] for track '136' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [714-715] for track '136' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-719] for track '137' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-714] for track '138' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-714] for track '139' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-719] for track '139' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [713-714] for track '140' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [713-719] for track '141' has 2 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '92' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '92' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '93' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '93' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '94' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '94' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '95' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '95' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '96' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '96' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '97' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '97' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '98' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '98' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '99' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '99' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '100' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '100' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '101' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '101' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '102' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '102' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '103' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '103' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '104' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '104' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '105' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '105' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '106' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '106' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '107' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '107' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '108' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '108' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '109' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '109' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '110' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '110' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '111' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '111' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '112' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '112' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '113' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '113' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '114' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '114' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '115' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '115' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '116' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '116' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '117' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '117' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '118' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '118' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '119' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '119' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '120' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '120' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '121' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '121' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '122' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '122' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '123' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '123' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '124' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '124' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '125' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '125' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '126' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '126' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '127' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '127' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '128' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '128' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '129' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '129' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '130' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '130' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '131' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '131' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '132' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '132' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '133' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '133' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '134' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '134' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '135' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '135' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '136' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '136' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '137' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '137' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '138' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '138' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '139' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '139' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '140' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '140' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '141' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '141' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '142' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '142' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '143' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '143' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_45'; source metadata written as null.

</details>