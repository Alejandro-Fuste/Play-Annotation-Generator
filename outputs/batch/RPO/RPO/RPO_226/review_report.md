# Play-Annotation-Generator Annotation Review — RPO_226

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_226`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `23` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `1` | 69 | START | 69 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `14` | 69 | START | 69 | 87 |
| ✅ EXACT | `Action_ZoneBlock` | C | `6` | `6` | 69 | START | 69 | 137 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 69 | START | 69 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `9` | 69 | START | 69 | 79 |
| ✅ EXACT | `Action_ReadDefender` | QB | `4` | `4` | 74 | START | 74 | 94 |
| ✅ EXACT | `Action_PullBall` | QB | `4` | `4` | 95 | START | 95 | 103 |
| ✅ EXACT | `Action_ThrowPass` | QB | `4` | `4` | 127 | START | 127 | 137 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 74 | 94 | 21 | inferred_complete_timeline |
| `Action_PullBall` | 95 | 103 | 9 | inferred_complete_timeline |
| `Action_None` | 104 | 126 | 23 | inferred_complete_timeline |
| `Action_ThrowPass` | 127 | 137 | 11 | inferred_complete_timeline |
| `Action_None` | 138 | 184 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 138 | 71 | inferred_complete_timeline |
| `Action_None` | 143 | 296 | 154 | inferred_complete_timeline |
| `Action_None` | 298 | 329 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 329 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 68 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 87 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 68 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 137 | 69 | inferred_complete_timeline |
| `Action_None` | 138 | 249 | 112 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 68 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 137 | 69 | inferred_complete_timeline |
| `Action_None` | 138 | 270 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 68 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 109 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 137 | 20 | inferred_complete_timeline |
| `Action_None` | 138 | 145 | 8 | inferred_complete_timeline |
| `Action_None` | 149 | 160 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 68 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 79 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 137 | 17 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 329 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 119 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 113 | 46 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 128 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 329 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 224 | 157 | inferred_complete_timeline |
| `Action_None` | 226 | 232 | 7 | inferred_complete_timeline |
| `Action_None` | 235 | 240 | 6 | inferred_complete_timeline |
| `Action_None` | 266 | 274 | 9 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 242 | 175 | inferred_complete_timeline |
| `Action_None` | 245 | 248 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 88–329 | 197 | 8 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 93–329 | 229 | 5 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 125–162 | 35 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 126–129 | 4 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 137–215 | 77 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 148–329 | 128 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 161–230 | 70 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 162–329 | 168 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 164–329 | 163 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 165–171 | 5 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 170–329 | 157 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 189–267 | 79 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 302–329 | 28 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 56 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' for track '0' starts at frame 68, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [68-329] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-81] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-137] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-240] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-274] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-270] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-249] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-128] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-242] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-138] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-296] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-87] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-267] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-306] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-324] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-172] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-213] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-230] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-297] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-329] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-329] for track '27' has 1 frames without a visible bounding box.
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

</details>