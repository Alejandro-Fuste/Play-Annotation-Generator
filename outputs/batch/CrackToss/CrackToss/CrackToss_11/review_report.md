# Play-Annotation-Generator Annotation Review — CrackToss_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_11`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 2
- **Group Expanded Events:** 1
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB3 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `20` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ START CHANGED | `Action_Toss` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | CB3 | `14` | `13` | 112 | START | 112 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `3` | `2` | 115 | START | 115 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `20` | `18` | 115 | START | 123 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | Position_Unknown | `16` | `15` | 117 | END | 112 | 113 |
| ⚠️ START CHANGED | `Action_Toss` | Position_Unknown | `16` | `15` | 122 | START | 127 | 146 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `1` | `0` | 147 | START | 147 | 211 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 215 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 26 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 111 | 20 | inferred_complete_timeline |
| `Action_None` | 112 | 121 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 188 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 152 | 41 | inferred_complete_timeline |
| `Action_None` | 155 | 213 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 181 | 70 | inferred_complete_timeline |
| `Action_None` | 183 | 249 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 97 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 111 | 9 | inferred_complete_timeline |
| `Action_None` | 112 | 142 | 31 | inferred_complete_timeline |
| `Action_None` | 148 | 174 | 27 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 269 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_BallSnap` | 112 | 117 | 6 | inferred_complete_timeline |
| `Action_None` | 118 | 118 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 189 | 78 | inferred_complete_timeline |
| `Action_None` | 192 | 201 | 10 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 213 | 6 | inferred_complete_timeline |
| `Action_None` | 221 | 269 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–211 | 212 | 2 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–154 | 144 | 5 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–269 | 249 | 6 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–247 | 248 | 2 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–218 | 206 | 6 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 6–231 | 200 | 11 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 18–144 | 50 | 6 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 122–123 | 2 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 123–269 | 144 | 5 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 128–138 | 8 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 131–135 | 5 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 132–144 | 13 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 133–153 | 11 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 148–183 | 29 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 148–204 | 51 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 171–254 | 83 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 181–269 | 85 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 191–195 | 5 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 197–257 | 61 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 213–269 | 57 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 217–269 | 53 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 220–228 | 9 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 223–269 | 47 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 223–269 | 47 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 225–269 | 45 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 227–269 | 43 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 230–269 | 40 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 235–254 | 12 | 3 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 252–253 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `16` (2 segments found)
- ⚠️ `Action_Toss` for actor_track_id `16` (Position_Unknown): Annotated start 122 != Inferred start 127

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 24: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 24: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '18' (Unknown) duration 93 frames exceeds threshold 90 frames [start=123, end=215].
- ⚠️ Action 'Action_BallCarry' range [147-211] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [115-133] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [136-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [141-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [151-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-249] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-152] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-213] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-152] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-223] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-269] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-247] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-97] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-194] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 118, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [118-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-21] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-47] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-107] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [112-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-108] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-119] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-141] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [123-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [147-202] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [204-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [210-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-144] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-174] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-158] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-233] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-254] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-269] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-269] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-240] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-269] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>