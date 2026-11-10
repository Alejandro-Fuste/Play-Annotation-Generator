# Play-Annotation-Generator Annotation Review — RPO_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_76`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 1
- **Action Segments:** 115
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `24` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_RunBlock` | LT | `0` | `0` | 39 | START | 39 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `10` | `10` | 39 | START | 44 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `13` | `13` | 39 | START | 39 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `7` | `7` | 39 | START | 39 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `8` | `8` | 39 | START | 39 | 47 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `5` | 42 | START | 42 | 60 |
| ✅ EXACT | `Action_PullBall` | QB | `5` | `5` | 61 | START | 61 | 68 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 100 | START | 100 | 114 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 42 | 60 | 19 | inferred_complete_timeline |
| `Action_PullBall` | 61 | 68 | 8 | inferred_complete_timeline |
| `Action_None` | 69 | 99 | 31 | inferred_complete_timeline |
| `Action_ThrowPass` | 100 | 114 | 15 | inferred_complete_timeline |
| `Action_None` | 115 | 158 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 88 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 78 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 39 | 113 | 75 | inferred_complete_timeline |
| `Action_None` | 115 | 186 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 39 | 51 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 55 | 114 | 60 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 44 | 68 | 25 | inferred_complete_timeline |
| `Action_RunBlock` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 39 | 51 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 62 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 65 | 92 | 28 | inferred_complete_timeline |
| `Action_RunBlock` | 94 | 114 | 21 | inferred_complete_timeline |
| `Action_None` | 115 | 128 | 14 | inferred_complete_timeline |
| `Action_None` | 131 | 172 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 39 | 47 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 74 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 90 | 106 | 17 | inferred_complete_timeline |
| `Action_None` | 115 | 166 | 52 | inferred_complete_timeline |
| `Action_None` | 170 | 213 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 62 | 25 | inferred_complete_timeline |
| `Action_None` | 64 | 77 | 14 | inferred_complete_timeline |
| `Action_None` | 79 | 110 | 32 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 86 | 49 | inferred_complete_timeline |
| `Action_None` | 88 | 117 | 30 | inferred_complete_timeline |
| `Action_None` | 135 | 212 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 18 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_None` | 38 | 45 | 8 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 78 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 58 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 92 | 55 | inferred_complete_timeline |
| `Action_None` | 94 | 136 | 43 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 150 | 8 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_None` | 159 | 165 | 7 | inferred_complete_timeline |
| `Action_None` | 168 | 231 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 79 | 42 | inferred_complete_timeline |
| `Action_None` | 81 | 124 | 44 | inferred_complete_timeline |
| `Action_None` | 126 | 282 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 38–61 | 12 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 50–166 | 110 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 61–97 | 33 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 68–153 | 28 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 75–162 | 73 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 86–171 | 77 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 94–299 | 206 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 97–248 | 152 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 97–202 | 103 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 100–104 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 103–180 | 78 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 116–165 | 50 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 125–174 | 44 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 143–299 | 157 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 144–165 | 21 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 144–299 | 156 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 148–207 | 40 | 3 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 164–299 | 136 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 175–299 | 125 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 210–212 | 3 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 281–296 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `28` | `31` | 131 | 131 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `8` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 87 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_RunBlock' range [39-113] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-186] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-78] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-231] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-158] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-79] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-124] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-282] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [39-51] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [54-62] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [65-92] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [94-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [39-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-74] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [76-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [87-88] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [90-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-166] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-213] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-62] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-110] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 38, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [38-38] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [44-68] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [70-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-212] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-58] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [39-51] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [55-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-143] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-166] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-97] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-248] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-165] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-159] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-162] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-189] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-296] for track '36' has 1 frames without a visible bounding box.
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

</details>