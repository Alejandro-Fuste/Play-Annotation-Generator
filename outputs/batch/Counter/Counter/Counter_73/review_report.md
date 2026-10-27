# Play-Annotation-Generator Annotation Review — Counter_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_73`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Fumble`
- **Result Frame:** 329
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 179
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `18` | `16` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR2 | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `20` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `13` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `15` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 19 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 56 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 145 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `12` | `11` | 143 | START | 143 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 148 | START | 154 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `18` | `16` | 148 | START | 148 | 155 |
| ✅ EXACT | `Action_DownBlock` | RT | `19` | `17` | 148 | START | 148 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR2 | `2` | `1` | 148 | START | 148 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `20` | `18` | 148 | START | 153 | 155 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `13` | 153 | END | 143 | 153 |
| ✅ EXACT | `Action_BallCarry` | QB | `15` | `13` | 179 | START | 179 | 218 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 223 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 19–218
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 142 | 124 | inferred_complete_timeline |
| `Action_SnapReceive` | 143 | 153 | 11 | inferred_complete_timeline |
| `Action_None` | 154 | 178 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 179 | 218 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 56–278
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 56 | 142 | 87 | inferred_complete_timeline |
| `Action_None` | 143 | 188 | 46 | inferred_complete_timeline |
| `Action_None` | 190 | 278 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 257 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PullBlock` | 148 | 206 | 59 | inferred_complete_timeline |
| `Action_PullBlock` | 208 | 223 | 16 | inferred_complete_timeline |
| `Action_None` | 224 | 250 | 27 | inferred_complete_timeline |
| `Action_None` | 252 | 288 | 37 | inferred_complete_timeline |
| `Action_None` | 290 | 322 | 33 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 153–199
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PullLeadBlock` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 163 | 172 | 10 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 197 | 199 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_BallSnap` | 143 | 146 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 223 | 8 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 145–158
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 155 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 158 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 148–155
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_DownBlock` | 148 | 155 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 12 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 35 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 46 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 142 | 78 | inferred_complete_timeline |
| `Action_None` | 143 | 214 | 72 | inferred_complete_timeline |
| `Action_None` | 217 | 222 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 285 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |
| `Action_None` | 215 | 329 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 27 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 35 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 282 | 140 | inferred_complete_timeline |
| `Action_None` | 284 | 329 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 265 | 123 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–226 | 227 | 2 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–329 | 265 | 19 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 35–118 | 33 | 5 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 160–164 | 5 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 201–279 | 43 | 2 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 219–235 | 16 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 220–268 | 13 | 2 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 232–329 | 75 | 4 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 242–277 | 36 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 245–260 | 8 | 3 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 247–276 | 30 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 252–316 | 39 | 6 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 259–329 | 67 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 259–262 | 4 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 262–298 | 28 | 4 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 268–329 | 62 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 273–275 | 3 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 277–329 | 49 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 280–329 | 36 | 5 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 281–329 | 47 | 2 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 291–329 | 37 | 3 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 294–296 | 3 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 300–319 | 17 | 4 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 301–329 | 29 | 1 | Undefined position; Undefined team |
| `42` | `63` | Position_Unknown | Team_Unknown | 311–325 | 14 | 2 | Undefined position; Undefined team |
| `43` | `67` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `20` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 117 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [143–153], lower_priority='Action_DownBlock' annotated_start=148, effective_Action_DownBlock_start=154.
- ⚠️ Action 'Action_None' range [143-226] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [148-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-288] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-322] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-282] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-257] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-265] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-285] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-33] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-44] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-63] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-71] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-172] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-184] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-264] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-284] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-8] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-35] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-19] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-27] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [143-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [154-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [216-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-142] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [179-218] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-188] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-278] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [153-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [163-172] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [184-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [190-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [197-199] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-279] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-268] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-243] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-303] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-277] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-276] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-289] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-309] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-304] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-283] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-311] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-293] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-307] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-329] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-329] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-322] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>