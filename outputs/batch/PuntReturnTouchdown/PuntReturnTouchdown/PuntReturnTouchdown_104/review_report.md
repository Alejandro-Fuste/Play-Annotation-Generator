# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_104

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_104`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 79
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 251
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 139
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_CrossGoalLine` | Right_Tackle | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `16` | `Group` | 0 | START | 0 | 229 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `8` | `8` | 1 | START | 1 | 56 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 33 | END | 33 | 33 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 57 | START | 57 | 73 |
| ✅ EXACT | `Action_CrossGoalLine` | Right_Tackle | `16` | `16` | 298 | START | 298 | 299 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 33 | 33 | inferred_complete_timeline |
| `Action_None` | 39 | 66 | 28 | inferred_complete_timeline |
| `Action_None` | 70 | 102 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 61 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 56 | 56 | inferred_complete_timeline |
| `Action_None` | 57 | 104 | 48 | inferred_complete_timeline |
| `Action_None` | 111 | 163 | 53 | inferred_complete_timeline |
| `Action_None` | 167 | 193 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 121 | 121 | inferred_complete_timeline |
| `Action_None` | 124 | 180 | 57 | inferred_complete_timeline |
| `Action_None` | 184 | 256 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 49 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 58 | 58 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 68 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_None` | 34 | 56 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 57 | 73 | 17 | inferred_complete_timeline |
| `Action_None` | 74 | 103 | 30 | inferred_complete_timeline |
| `Action_None` | 105 | 234 | 130 | inferred_complete_timeline |
| `Action_None` | 247 | 259 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 154 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 297 | 55 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 47 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 94 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 72 | 72 | inferred_complete_timeline |
| `Action_None` | 76 | 88 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 70 | 70 | inferred_complete_timeline |
| `Action_None` | 78 | 135 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 105 | 105 | inferred_complete_timeline |
| `Action_None` | 109 | 257 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 136 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 194 | 194 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 35–208 | 173 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 37–249 | 182 | 7 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 54–66 | 13 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 57–62 | 5 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 67–114 | 48 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 75–250 | 150 | 4 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 79–299 | 219 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 81–148 | 55 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 106–107 | 2 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 107–299 | 185 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 113–256 | 124 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 119–253 | 131 | 3 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 120–257 | 138 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 125–141 | 14 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 138–152 | 15 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 142–270 | 112 | 7 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 147–154 | 7 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 160–217 | 34 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 160–257 | 98 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 160–162 | 3 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 167–202 | 28 | 5 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 167–259 | 93 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 168–299 | 71 | 2 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 176–256 | 53 | 5 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 217–299 | 77 | 2 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 244–257 | 14 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 249–254 | 4 | 2 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `47` | `74` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `48` | `75` | Position_Unknown | Team_Unknown | 258–299 | 42 | 1 | Undefined position; Undefined team |
| `49` | `76` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `51` | `79` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `52` | `80` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `53` | `81` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `54` | `82` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `55` | `83` | Position_Unknown | Team_Unknown | 258–263 | 6 | 1 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 260–299 | 40 | 1 | Undefined position; Undefined team |
| `57` | `87` | Position_Unknown | Team_Unknown | 260–263 | 4 | 1 | Undefined position; Undefined team |
| `58` | `92` | Position_Unknown | Team_Unknown | 261–263 | 3 | 1 | Undefined position; Undefined team |
| `59` | `93` | Position_Unknown | Team_Unknown | 261–263 | 3 | 1 | Undefined position; Undefined team |
| `60` | `94` | Position_Unknown | Team_Unknown | 261–263 | 3 | 1 | Undefined position; Undefined team |
| `61` | `95` | Position_Unknown | Team_Unknown | 261–263 | 3 | 1 | Undefined position; Undefined team |
| `62` | `96` | Position_Unknown | Team_Unknown | 261–299 | 4 | 2 | Undefined position; Undefined team |
| `63` | `97` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `64` | `98` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `65` | `101` | Position_Unknown | Team_Unknown | 264–277 | 14 | 1 | Undefined position; Undefined team |
| `66` | `102` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `67` | `105` | Position_Unknown | Team_Unknown | 264–299 | 36 | 1 | Undefined position; Undefined team |
| `68` | `106` | Position_Unknown | Team_Unknown | 264–290 | 27 | 1 | Undefined position; Undefined team |
| `69` | `112` | Position_Unknown | Team_Unknown | 265–295 | 31 | 1 | Undefined position; Undefined team |
| `70` | `130` | Position_Unknown | Team_Unknown | 268–299 | 32 | 1 | Undefined position; Undefined team |
| `71` | `132` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `72` | `133` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `73` | `134` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `74` | `136` | Position_Unknown | Team_Unknown | 271–299 | 29 | 1 | Undefined position; Undefined team |
| `75` | `139` | Position_Unknown | Team_Unknown | 272–282 | 11 | 1 | Undefined position; Undefined team |
| `76` | `143` | Position_Unknown | Team_Unknown | 274–282 | 9 | 1 | Undefined position; Undefined team |
| `77` | `144` | Position_Unknown | Team_Unknown | 290–299 | 10 | 1 | Undefined position; Undefined team |
| `78` | `145` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 62 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 62 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 124 |
| Missing visible bounding boxes during action | 124 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [1-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-61] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-136] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-58] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-121] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-256] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-94] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-234] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-259] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-104] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-72] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-88] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-154] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-33] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-299] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-135] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-257] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-204] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-188] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-220] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-249] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-114] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-127] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-120] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-148] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-222] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-299] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-172] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-256] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-230] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-253] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-141] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-175] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-203] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-235] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-270] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-191] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-257] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-259] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-194] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-256] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-259] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-299] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-257] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-299] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-263] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-277] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-290] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-295] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-299] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-282] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-282] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>