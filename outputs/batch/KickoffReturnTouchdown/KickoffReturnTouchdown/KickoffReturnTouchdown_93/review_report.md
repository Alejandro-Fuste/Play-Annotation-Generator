# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_93`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 74
- **Ball Tracks:** 0
- **Action Segments:** 168
- **Validation Warnings:** 238
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 153
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `11` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `13` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `15` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `18` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `19` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `21` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `5` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `6` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `7` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `8` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `9` | `Group` | 0 | START | 0 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `7` | `7` | 31 | START | 31 | 60 |
| ✅ EXACT | `Action_KickBall` | Kicker | `7` | `7` | 66 | START | 66 | 70 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `2` | `2` | 175 | START | 175 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `2` | `2` | 190 | START | 190 | 241 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | `2` | `2` | 538 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_KickApproach` | 31 | 60 | 30 | inferred_complete_timeline |
| `Action_KickApproach` | 62 | 65 | 4 | inferred_complete_timeline |
| `Action_KickBall` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_None` | 71 | 160 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 100 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 64 | 34 | inferred_complete_timeline |
| `Action_None` | 66 | 157 | 92 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_None` | 187 | 198 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 157 | 127 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_None` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 159 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 113 | 83 | inferred_complete_timeline |
| `Action_None` | 116 | 143 | 28 | inferred_complete_timeline |
| `Action_None` | 147 | 163 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–458
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 40 | 10 | inferred_complete_timeline |
| `Action_None` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_None` | 46 | 458 | 413 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 196 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 212 | 182 | inferred_complete_timeline |
| `Action_None` | 218 | 237 | 20 | inferred_complete_timeline |
| `Action_None` | 240 | 246 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 63 | 33 | inferred_complete_timeline |
| `Action_None` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_None` | 93 | 103 | 11 | inferred_complete_timeline |
| `Action_None` | 113 | 140 | 28 | inferred_complete_timeline |
| `Action_None` | 145 | 155 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 155 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 139 | 109 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 158 | 10 | inferred_complete_timeline |
| `Action_None` | 171 | 182 | 12 | inferred_complete_timeline |
| `Action_None` | 194 | 212 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 86 | 56 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 128 | 27 | inferred_complete_timeline |
| `Action_None` | 130 | 158 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_None` | 37 | 68 | 32 | inferred_complete_timeline |
| `Action_None` | 71 | 79 | 9 | inferred_complete_timeline |
| `Action_None` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_None` | 158 | 215 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 86 | 56 | inferred_complete_timeline |
| `Action_None` | 95 | 116 | 22 | inferred_complete_timeline |
| `Action_None` | 120 | 260 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 153 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_CatchKick` | 175 | 183 | 9 | inferred_complete_timeline |
| `Action_None` | 184 | 189 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 241 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 253 | 255 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 134 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 276 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 179 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 267 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 256 | 226 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 6–247 | 158 | 10 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 49–157 | 67 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 114–125 | 12 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 119–198 | 67 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 125–157 | 25 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 129–200 | 17 | 5 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 144–203 | 57 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 158–176 | 19 | 1 | Undefined position; Undefined team |
| `30` | `86` | Position_Unknown | Team_Unknown | 163–240 | 75 | 2 | Undefined position; Undefined team |
| `31` | `110` | Position_Unknown | Team_Unknown | 167–178 | 12 | 1 | Undefined position; Undefined team |
| `32` | `144` | Position_Unknown | Team_Unknown | 174–277 | 104 | 1 | Undefined position; Undefined team |
| `33` | `147` | Position_Unknown | Team_Unknown | 175–196 | 22 | 1 | Undefined position; Undefined team |
| `34` | `148` | Position_Unknown | Team_Unknown | 175–188 | 14 | 1 | Undefined position; Undefined team |
| `35` | `149` | Position_Unknown | Team_Unknown | 175–202 | 23 | 2 | Undefined position; Undefined team |
| `36` | `151` | Position_Unknown | Team_Unknown | 177–349 | 171 | 2 | Undefined position; Undefined team |
| `37` | `152` | Position_Unknown | Team_Unknown | 177–196 | 19 | 2 | Undefined position; Undefined team |
| `38` | `153` | Position_Unknown | Team_Unknown | 179–194 | 16 | 1 | Undefined position; Undefined team |
| `39` | `156` | Position_Unknown | Team_Unknown | 185–254 | 51 | 4 | Undefined position; Undefined team |
| `40` | `167` | Position_Unknown | Team_Unknown | 200–209 | 6 | 2 | Undefined position; Undefined team |
| `41` | `168` | Position_Unknown | Team_Unknown | 200–283 | 84 | 1 | Undefined position; Undefined team |
| `42` | `179` | Position_Unknown | Team_Unknown | 211–238 | 28 | 1 | Undefined position; Undefined team |
| `43` | `181` | Position_Unknown | Team_Unknown | 221–251 | 23 | 4 | Undefined position; Undefined team |
| `44` | `182` | Position_Unknown | Team_Unknown | 230–539 | 310 | 1 | Undefined position; Undefined team |
| `45` | `187` | Position_Unknown | Team_Unknown | 235–358 | 124 | 1 | Undefined position; Undefined team |
| `46` | `188` | Position_Unknown | Team_Unknown | 235–337 | 103 | 1 | Undefined position; Undefined team |
| `47` | `189` | Position_Unknown | Team_Unknown | 238–285 | 48 | 1 | Undefined position; Undefined team |
| `48` | `191` | Position_Unknown | Team_Unknown | 239–289 | 51 | 1 | Undefined position; Undefined team |
| `49` | `192` | Position_Unknown | Team_Unknown | 239–359 | 121 | 1 | Undefined position; Undefined team |
| `50` | `193` | Position_Unknown | Team_Unknown | 243–244 | 2 | 1 | Undefined position; Undefined team |
| `51` | `194` | Position_Unknown | Team_Unknown | 244–258 | 15 | 1 | Undefined position; Undefined team |
| `52` | `195` | Position_Unknown | Team_Unknown | 248–539 | 292 | 1 | Undefined position; Undefined team |
| `53` | `196` | Position_Unknown | Team_Unknown | 251–461 | 211 | 1 | Undefined position; Undefined team |
| `54` | `200` | Position_Unknown | Team_Unknown | 306–350 | 45 | 1 | Undefined position; Undefined team |
| `55` | `202` | Position_Unknown | Team_Unknown | 308–341 | 34 | 1 | Undefined position; Undefined team |
| `56` | `203` | Position_Unknown | Team_Unknown | 323–326 | 4 | 1 | Undefined position; Undefined team |
| `57` | `204` | Position_Unknown | Team_Unknown | 378–413 | 32 | 2 | Undefined position; Undefined team |
| `58` | `206` | Position_Unknown | Team_Unknown | 379–434 | 52 | 2 | Undefined position; Undefined team |
| `59` | `207` | Position_Unknown | Team_Unknown | 381–426 | 40 | 3 | Undefined position; Undefined team |
| `60` | `208` | Position_Unknown | Team_Unknown | 396–539 | 144 | 1 | Undefined position; Undefined team |
| `61` | `209` | Position_Unknown | Team_Unknown | 396–539 | 144 | 1 | Undefined position; Undefined team |
| `62` | `211` | Position_Unknown | Team_Unknown | 423–469 | 47 | 1 | Undefined position; Undefined team |
| `63` | `213` | Position_Unknown | Team_Unknown | 444–448 | 5 | 1 | Undefined position; Undefined team |
| `64` | `214` | Position_Unknown | Team_Unknown | 451–455 | 5 | 1 | Undefined position; Undefined team |
| `65` | `216` | Position_Unknown | Team_Unknown | 457–539 | 83 | 1 | Undefined position; Undefined team |
| `66` | `217` | Position_Unknown | Team_Unknown | 465–539 | 75 | 1 | Undefined position; Undefined team |
| `67` | `218` | Position_Unknown | Team_Unknown | 477–539 | 63 | 1 | Undefined position; Undefined team |
| `68` | `220` | Position_Unknown | Team_Unknown | 491–539 | 49 | 1 | Undefined position; Undefined team |
| `69` | `221` | Position_Unknown | Team_Unknown | 495–539 | 45 | 1 | Undefined position; Undefined team |
| `70` | `222` | Position_Unknown | Team_Unknown | 501–539 | 39 | 1 | Undefined position; Undefined team |
| `71` | `223` | Position_Unknown | Team_Unknown | 503–539 | 37 | 1 | Undefined position; Undefined team |
| `72` | `225` | Position_Unknown | Team_Unknown | 509–539 | 31 | 1 | Undefined position; Undefined team |
| `73` | `227` | Position_Unknown | Team_Unknown | 533–537 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `2` (Kick_Returner1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ 52 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 52 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 104 |
| Missing visible bounding boxes during action | 132 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '2' has invalid range: start=538, end=255. Clamping end to start.
- ⚠️ Action 'Action_None' range [31-267] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-276] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-241] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [253-255] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-134] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-128] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-212] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-237] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-246] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-40] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-458] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [31-60] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-160] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-113] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-256] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-196] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-153] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-103] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-140] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-260] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-139] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-23] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-215] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-25] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-231] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-157] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-158] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-176] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-192] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-240] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-178] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-277] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-188] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-195] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-257] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-349] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-196] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-194] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-219] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-254] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-283] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-238] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-248] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-358] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-337] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-285] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-289] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-359] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-258] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-461] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-350] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-341] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-395] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-413] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-408] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-434] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-407] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-426] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-469] for track '62' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-448] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-455] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-539] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-537] for track '73' has 1 frames without a visible bounding box.
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

</details>