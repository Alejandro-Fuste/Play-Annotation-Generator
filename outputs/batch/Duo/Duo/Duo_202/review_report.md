# Play-Annotation-Generator Annotation Review — Duo_202

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_202`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_ComboBlock` | DT3 | defense | `15` | `15` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `13` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `6` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `12` | `12` | 63 | START | 63 | 79 |
| ✅ EXACT | `Action_ComboBlock` | LT | `13` | `13` | 63 | START | 63 | 84 |
| ⚠️ START CHANGED | `Action_ComboBlock` | DT3 | `15` | `15` | 63 | START | 86 | 109 |
| ✅ EXACT | `Action_ComboBlock` | LG | `3` | `3` | 63 | START | 63 | 109 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `13` | `13` | 85 | START | 85 | 109 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 109 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–6
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 6 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 95 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 55 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 175 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 175 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ComboBlock` | 63 | 84 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 85 | 109 | 25 | inferred_complete_timeline |
| `Action_None` | 110 | 175 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ComboBlock` | 63 | 109 | 47 | inferred_complete_timeline |
| `Action_None` | 110 | 163 | 54 | inferred_complete_timeline |
| `Action_None` | 166 | 175 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ComboBlock` | 63 | 79 | 17 | inferred_complete_timeline |
| `Action_ComboBlock` | 81 | 107 | 27 | inferred_complete_timeline |
| `Action_ComboBlock` | 109 | 109 | 1 | inferred_complete_timeline |
| `Action_None` | 110 | 175 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 156 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 175 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 131 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ComboBlock` | 86 | 109 | 24 | inferred_complete_timeline |
| `Action_None` | 110 | 124 | 15 | inferred_complete_timeline |
| `Action_None` | 126 | 175 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 122 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 140 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 175 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 104 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 117 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 140 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 170 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 129 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 175 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–137 | 127 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 6–117 | 75 | 8 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 10–175 | 149 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 13–16 | 4 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 56–175 | 115 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 68–96 | 6 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 87–175 | 81 | 5 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 111–157 | 45 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 118–175 | 53 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 135–142 | 6 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 144–169 | 10 | 4 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 162–175 | 14 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 166–175 | 10 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 170–175 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `12` (3 segments found)
- ⚠️ `Action_ComboBlock` for actor_track_id `15` (DT3): Annotated start 63 != Inferred start 86

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 406: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-90] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-104] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-133] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-152] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-170] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-95] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-131] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [63-79] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [81-107] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-175] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-129] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-175] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-175] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-15] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-60] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-94] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-102] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-17] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-175] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-16] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-175] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-146] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-155] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-157] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-175] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-175] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-175] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>