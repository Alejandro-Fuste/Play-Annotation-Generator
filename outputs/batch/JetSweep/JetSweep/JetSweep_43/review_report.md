# Play-Annotation-Generator Annotation Review — JetSweep_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 1
- **Action Segments:** 77
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `13` | `12` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 94 |
| ✅ EXACT | `Action_LeadBlock` | RB | `13` | `12` | 45 | START | 45 | 97 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `16` | `15` | 53 | START | 53 | 70 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `10` | `9` | 58 | END | 93 | 93 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 65 | START | 65 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `16` | `15` | 71 | START | 72 | 141 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `1` | `0` | 77 | START | 77 | 94 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 93 | START | 93 | 93 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 95 | START | 95 | 97 |
| ✅ EXACT | `Action_ZoneBlock` | C | `14` | `13` | 95 | START | 95 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `6` | 95 | START | 95 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 95 | START | 95 | 97 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 95 | START | 95 | 97 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 97 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_Toss` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 92 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 93 | 93 | 1 | inferred_complete_timeline |
| `Action_None` | 94 | 107 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_LeadBlock` | 45 | 97 | 53 | inferred_complete_timeline |
| `Action_None` | 98 | 120 | 23 | inferred_complete_timeline |
| `Action_None` | 125 | 196 | 72 | inferred_complete_timeline |
| `Action_None` | 198 | 207 | 10 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 77 | 94 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 98 | 135 | 38 | inferred_complete_timeline |
| `Action_None` | 144 | 210 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 98 | 147 | 50 | inferred_complete_timeline |
| `Action_None` | 152 | 158 | 7 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 92 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 93 | 93 | 1 | inferred_complete_timeline |
| `Action_None` | 94 | 94 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 98 | 113 | 16 | inferred_complete_timeline |
| `Action_None` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_None` | 126 | 146 | 21 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 98 | 111 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 98 | 105 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 166 | 74 | inferred_complete_timeline |
| `Action_None` | 169 | 210 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 102 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 210 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 210 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 196 | 104 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 108 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 109 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 33–210 | 173 | 5 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 109–210 | 81 | 5 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 115–210 | 96 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 115–210 | 94 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 128–135 | 8 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 136–210 | 75 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 138–210 | 72 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 162–210 | 49 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 176–210 | 35 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 188–210 | 23 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | 0 | 43 | 44 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '9' has invalid range: start=93, end=58. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '13' has invalid range: start=93, end=58. Clamping end to start.
- ⚠️ Action 'Action_None' range [98-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-102] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [65-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-196] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [53-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [72-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '27' has 1 frames without a visible bounding box.
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