# Play-Annotation-Generator Annotation Review — RPO_122

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_122`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunHitchRoute` | actor_track_id `28` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `20` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `11` | 45 | START | 45 | 50 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `12` | 45 | START | 45 | 48 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `13` | 45 | START | 45 | 108 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 45 | START | 45 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `2` | 45 | START | 45 | 81 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `9` | 51 | START | 51 | 59 |
| ✅ EXACT | `Action_PullBall` | QB | `9` | `9` | 60 | START | 60 | 66 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `20` | `17` | 102 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 50 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_PullBall` | 60 | 66 | 7 | inferred_complete_timeline |
| `Action_None` | 71 | 83 | 13 | inferred_complete_timeline |
| `Action_None` | 85 | 101 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 66 | 23 | inferred_complete_timeline |
| `Action_None` | 73 | 125 | 53 | inferred_complete_timeline |
| `Action_None` | 127 | 136 | 10 | inferred_complete_timeline |
| `Action_None` | 141 | 181 | 41 | inferred_complete_timeline |
| `Action_None` | 187 | 239 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 81 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 108 | 23 | inferred_complete_timeline |
| `Action_None` | 109 | 174 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 50 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_None` | 109 | 109 | 1 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 108 | 64 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 169 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 48 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 108 | 64 | inferred_complete_timeline |
| `Action_None` | 109 | 109 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 47 | 91 | 45 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 116 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 71 | 28 | inferred_complete_timeline |
| `Action_None` | 80 | 104 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 88 | 45 | inferred_complete_timeline |
| `Action_None` | 103 | 124 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 112 | 69 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_None` | 127 | 150 | 24 | inferred_complete_timeline |
| `Action_None` | 160 | 192 | 33 | inferred_complete_timeline |
| `Action_None` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 114 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 89 | 46 | inferred_complete_timeline |
| `Action_None` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 124 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 239 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 94 | 51 | inferred_complete_timeline |
| `Action_None` | 96 | 135 | 40 | inferred_complete_timeline |
| `Action_None` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_None` | 145 | 169 | 25 | inferred_complete_timeline |
| `Action_None` | 171 | 239 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–71 | 72 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 84–157 | 54 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 95–127 | 25 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 107–148 | 34 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 118–193 | 70 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 125–239 | 79 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 129–197 | 68 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 130–239 | 110 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 131–239 | 101 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 132–134 | 3 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 135–190 | 54 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 155–235 | 76 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 161–208 | 29 | 4 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 165–199 | 26 | 4 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 173–239 | 67 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 175–179 | 5 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 207–219 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `20` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 77 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [44-94] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-169] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-174] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-104] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-192] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-114] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-124] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-71] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [60-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-83] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-66] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-181] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 109, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [109-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-169] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 109, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [109-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-157] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-115] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-132] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-186] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-174] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-197] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-176] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-187] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-219] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>