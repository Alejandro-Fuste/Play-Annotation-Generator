# Play-Annotation-Generator Annotation Review — RPO_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_53`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `2` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 3 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 6 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 59 | START | 59 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 59 | START | 59 | 60 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 59 | START | 59 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `16` | 59 | START | 59 | 102 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 59 | START | 59 | 99 |
| ✅ EXACT | `Action_ReadDefender` | QB | `11` | `11` | 60 | START | 60 | 78 |
| ✅ EXACT | `Action_PullBall` | QB | `11` | `11` | 79 | START | 79 | 86 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 102 | START | 102 | 111 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 60 | 78 | 19 | inferred_complete_timeline |
| `Action_PullBall` | 79 | 86 | 8 | inferred_complete_timeline |
| `Action_None` | 87 | 101 | 15 | inferred_complete_timeline |
| `Action_ThrowPass` | 102 | 111 | 10 | inferred_complete_timeline |
| `Action_None` | 112 | 180 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 76 | 19 | inferred_complete_timeline |
| `Action_None` | 78 | 106 | 29 | inferred_complete_timeline |
| `Action_None` | 113 | 122 | 10 | inferred_complete_timeline |
| `Action_None` | 133 | 136 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 160 | 103 | inferred_complete_timeline |
| `Action_None` | 166 | 174 | 9 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 80 | 23 | inferred_complete_timeline |
| `Action_None` | 90 | 106 | 17 | inferred_complete_timeline |
| `Action_None` | 114 | 150 | 37 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 3–108
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 102 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 108 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 6–99
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 20 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 57 | 36 | inferred_complete_timeline |
| `Action_None` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 99 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_None` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 80 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 94 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_None` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_None` | 128 | 141 | 14 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 155 | 10 | inferred_complete_timeline |
| `Action_None` | 157 | 178 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 106 | 27 | inferred_complete_timeline |
| `Action_None` | 141 | 177 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 83 | 25 | inferred_complete_timeline |
| `Action_None` | 131 | 180 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 7–166
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 15 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 57 | 15 | inferred_complete_timeline |
| `Action_None` | 58 | 166 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 6–70
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 17 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 32 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 50 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 57 | 5 | inferred_complete_timeline |
| `Action_None` | 58 | 70 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 6–180
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 19 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 32 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_None` | 60 | 72 | 13 | inferred_complete_timeline |
| `Action_None` | 76 | 79 | 4 | inferred_complete_timeline |
| `Action_None` | 81 | 86 | 6 | inferred_complete_timeline |
| `Action_None` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_None` | 97 | 180 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 106 | 49 | inferred_complete_timeline |
| `Action_None` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 99 | 42 | inferred_complete_timeline |
| `Action_None` | 114 | 180 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 167 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 174 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 46–180 | 82 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 91–176 | 56 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 115–180 | 66 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 140–145 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 74 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [58-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-76] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-99] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-106] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [60-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-80] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-106] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-106] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-141] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-83] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-57] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-20] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-57] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-99] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-17] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-32] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-72] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-180] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-166] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-157] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>