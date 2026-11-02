# Play-Annotation-Generator Annotation Review — PinAndPull_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_4`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Touchdown`
- **Result Frame:** 328
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `24` | `19` |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | Team_Unknown | `25` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 111 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 78 | START | 78 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `24` | `19` | 81 | START | 81 | 94 |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | `25` | `20` | 81 | START | 83 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RG | `18` | `17` | 81 | START | 81 | 83 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 92 | END | 78 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `10` | `9` | 98 | START | 98 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 112 | START | 112 | 138 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 179 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 92 | 15 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 105 | 111 | 7 | inferred_complete_timeline |
| `Action_None` | 112 | 154 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 138 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 142 | 157 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 160 | 165 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 328 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 135 | 58 | inferred_complete_timeline |
| `Action_None` | 140 | 153 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 147 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 123 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_BallSnap` | 78 | 84 | 7 | inferred_complete_timeline |
| `Action_None` | 105 | 113 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 125 | 147 | 23 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 112 | 35 | inferred_complete_timeline |
| `Action_None` | 141 | 205 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 135 | 58 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 223 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 110 | 33 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 253 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 92 | 15 | inferred_complete_timeline |
| `Action_None` | 98 | 183 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 86 | 9 | inferred_complete_timeline |
| `Action_None` | 94 | 105 | 12 | inferred_complete_timeline |
| `Action_None` | 108 | 200 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 220 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 263 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 118 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 124 | 47 | inferred_complete_timeline |
| `Action_None` | 127 | 133 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 125 | 48 | inferred_complete_timeline |
| `Action_None` | 127 | 140 | 14 | inferred_complete_timeline |
| `Action_None` | 151 | 156 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 173 | 13 | inferred_complete_timeline |
| `Action_None` | 191 | 221 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 104 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `24` | Position_Unknown | Team_Unknown | 60–231 | 127 | 7 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 83–111 | 29 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 127–210 | 75 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 130–285 | 144 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 139–141 | 3 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 149–192 | 44 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 162–284 | 120 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 166–248 | 79 | 2 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 195–227 | 31 | 3 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 216–229 | 12 | 2 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 226–279 | 54 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 229–328 | 100 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 252–253 | 2 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 321–324 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `24` (4 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `25` (Position_Unknown): Annotated start 81 != Inferred start 83
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (Unknown) duration 99 frames exceeds threshold 90 frames [start=81, end=179].
- ⚠️ Action 'Action_None' range [78-123] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-135] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-263] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-269] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [160-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-328] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [98-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-86] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-105] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-200] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-221] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-220] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [78-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' for track '17' starts at frame 81, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PullLeadBlock' range [81-83] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [87-97] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [125-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-253] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [81-94] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [114-122] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-231] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [83-111] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-207] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-164] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-285] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-205] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-284] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-207] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-227] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-279] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '33' has 1 frames without a visible bounding box.
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

</details>