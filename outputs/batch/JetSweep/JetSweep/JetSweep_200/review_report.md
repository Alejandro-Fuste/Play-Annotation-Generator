# Play-Annotation-Generator Annotation Review — JetSweep_200

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_200`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `17` | `16` | 25 | START | 25 | 54 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 32 | START | 32 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `4` | `3` | 36 | START | 36 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 36 | START | 36 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 36 | START | 62 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `13` | 36 | START | 36 | 54 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `15` | `14` | 36 | START | 36 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `5` | 36 | START | 36 | 45 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 44 | END | 32 | 44 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 53 | START | 53 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `16` | 55 | START | 55 | 82 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 137 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 44 | 13 | inferred_complete_timeline |
| `Action_None` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_Toss` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 60 | 29 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_LeadBlock` | 36 | 100 | 65 | inferred_complete_timeline |
| `Action_LeadBlock` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_LeadBlock` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_LeadBlock` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_None` | 169 | 239 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 45 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 73 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 114 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 44 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 85 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 107 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 136 | 28 | inferred_complete_timeline |
| `Action_None` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_None` | 148 | 187 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 52 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 137 | 84 | inferred_complete_timeline |
| `Action_None` | 138 | 239 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 54 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 81 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 135 | 47 | inferred_complete_timeline |
| `Action_None` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 115 | 84 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 65 | 34 | inferred_complete_timeline |
| `Action_None` | 80 | 97 | 18 | inferred_complete_timeline |
| `Action_None` | 100 | 107 | 8 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 175 | 144 | inferred_complete_timeline |
| `Action_None` | 182 | 239 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_None` | 50 | 74 | 25 | inferred_complete_timeline |
| `Action_None` | 77 | 99 | 23 | inferred_complete_timeline |
| `Action_None` | 105 | 225 | 121 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 198 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 136 | 105 | inferred_complete_timeline |
| `Action_None` | 142 | 175 | 34 | inferred_complete_timeline |
| `Action_None` | 177 | 239 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 237 | 206 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 16–239 | 224 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 25–239 | 201 | 8 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 48–75 | 28 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 81–239 | 157 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 87–88 | 2 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 94–117 | 15 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 102–239 | 138 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 117–210 | 37 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 129–136 | 7 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 141–239 | 99 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 141–239 | 99 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 145–239 | 95 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 150–239 | 90 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 160–239 | 80 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 171–239 | 55 | 4 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 234–237 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `4` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '3' (TE) duration 102 frames exceeds threshold 90 frames [start=36, end=137].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 102 frames exceeds threshold 90 frames [start=36, end=137].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 102 frames exceeds threshold 90 frames [start=36, end=137].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [32–44], lower_priority='Action_ZoneBlock' annotated_start=36, effective_Action_ZoneBlock_start=45.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 102 frames exceeds threshold 90 frames [start=36, end=137].
- ⚠️ Action 'Action_None' range [32-65] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-97] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-107] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-198] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-136] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-175] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [36-100] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [112-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [118-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [122-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [136-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-45] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-237] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-60] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [32-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-187] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-239] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-114] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [25-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [55-82] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-99] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-210] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [213-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [234-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-75] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-198] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-106] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-213] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '30' has 1 frames without a visible bounding box.
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

</details>