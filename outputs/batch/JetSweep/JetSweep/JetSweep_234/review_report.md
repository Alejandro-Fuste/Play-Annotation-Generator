# Play-Annotation-Generator Annotation Review — JetSweep_234

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_234`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | offense | `5` | `4` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 62 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `19` | `18` | 59 | START | 60 | 89 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 62 | START | 62 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | `5` | `4` | 63 | START | 63 | 89 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `15` | 63 | START | 78 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `2` | 63 | START | 63 | 129 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 63 | START | 63 | 123 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 63 | START | 63 | 129 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `8` | 63 | START | 63 | 129 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 77 | END | 62 | 77 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 84 | START | 84 | 89 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `19` | `18` | 90 | START | 90 | 129 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 163 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_None` | 78 | 83 | 6 | inferred_complete_timeline |
| `Action_Toss` | 84 | 89 | 6 | inferred_complete_timeline |
| `Action_None` | 90 | 129 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 129 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 96 | 35 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_LeadBlock` | 63 | 89 | 27 | inferred_complete_timeline |
| `Action_LeadBlock` | 133 | 163 | 31 | inferred_complete_timeline |
| `Action_None` | 164 | 222 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 123 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 129 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 61 | 35 | inferred_complete_timeline |
| `Action_BallSnap` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 135 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 129 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 129 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 121 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 129 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 224 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 239 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 129 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 77 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 99 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 5–26 | 4 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 36–65 | 11 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 60–129 | 70 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 70–131 | 59 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 70–137 | 63 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 85–129 | 45 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 118–119 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 120–123 | 4 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 130–139 | 10 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 130–133 | 4 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 130–239 | 110 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 130–141 | 12 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 130–219 | 90 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 130–232 | 98 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 130–235 | 106 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 136–224 | 87 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 137–239 | 103 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 164–168 | 5 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 202–204 | 3 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 222–226 | 5 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 233–237 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `19` (Position_Unknown): Annotated start 59 != Inferred start 60
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `5` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 63 != Inferred start 78
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '4' (TE2) duration 101 frames exceeds threshold 90 frames [start=63, end=163].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [62–77], lower_priority='Action_ZoneBlock' annotated_start=63, effective_Action_ZoneBlock_start=78.
- ⚠️ Action 'Action_None' range [62-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-129] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [63-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [133-163] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-224] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-57] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-92] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-129] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-141] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-219] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-206] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-232] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-235] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-157] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-224] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '40' has 1 frames without a visible bounding box.
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