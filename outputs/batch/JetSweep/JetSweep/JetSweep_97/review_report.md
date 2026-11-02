# Play-Annotation-Generator Annotation Review — JetSweep_97

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_97`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `19` | `18` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Toss` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `19` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_JetMotion` | WR | `19` | `18` | 21 | START | 21 | 74 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 46 | START | 46 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `9` | 50 | START | 50 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `13` | 50 | START | 50 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 50 | START | 62 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `15` | 50 | START | 50 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `2` | `1` | 50 | START | 50 | 111 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 61 | END | 46 | 61 |
| ✅ EXACT | `Action_Toss` | QB | `17` | `16` | 69 | START | 69 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `19` | `18` | 75 | START | 75 | 102 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 111 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 61 | 16 | inferred_complete_timeline |
| `Action_None` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_Toss` | 69 | 74 | 6 | inferred_complete_timeline |
| `Action_None` | 75 | 129 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 110 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_JetMotion` | 21 | 74 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 75 | 102 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 159 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 108 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 210 | 165 | inferred_complete_timeline |
| `Action_None` | 213 | 243 | 31 | inferred_complete_timeline |
| `Action_None` | 250 | 302 | 53 | inferred_complete_timeline |
| `Action_None` | 305 | 329 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 111 | 62 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 111 | 62 | inferred_complete_timeline |
| `Action_None` | 112 | 121 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 61 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 111 | 50 | inferred_complete_timeline |
| `Action_None` | 112 | 119 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 111 | 62 | inferred_complete_timeline |
| `Action_None` | 112 | 130 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 111 | 62 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 110 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 110 | 65 | inferred_complete_timeline |
| `Action_None` | 112 | 117 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 96 | 51 | inferred_complete_timeline |
| `Action_None` | 102 | 115 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 123 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 187 | 142 | inferred_complete_timeline |
| `Action_None` | 195 | 329 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 102 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 128 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 231 | 186 | inferred_complete_timeline |
| `Action_None` | 235 | 243 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 119 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `21` | Position_Unknown | Team_Unknown | 95–114 | 13 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 131–218 | 88 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 138–143 | 6 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 153–220 | 66 | 2 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 167–294 | 128 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 171–292 | 106 | 5 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 182–184 | 3 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 207–329 | 123 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 219–329 | 111 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 222–329 | 104 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 242–321 | 74 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 248–329 | 63 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 258–292 | 35 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 262–329 | 68 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 262–329 | 68 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 298–329 | 32 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 308–329 | 22 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 311–329 | 19 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [46–61], lower_priority='Action_ZoneBlock' annotated_start=50, effective_Action_ZoneBlock_start=62.
- ⚠️ Action 'Action_None' range [46-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-231] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-128] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-96] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-243] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-110] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [75-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-159] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-218] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-220] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-294] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-261] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-279] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-292] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-301] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-295] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-311] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-292] for track '32' has 2 frames without a visible bounding box.
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

</details>