# Play-Annotation-Generator Annotation Review — RPO_139

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_139`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `3` | source `Route` | no temporal frame

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
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `11` | 81 | START | 81 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 81 | START | 107 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 81 | START | 81 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 81 | START | 81 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 81 | START | 81 | 95 |
| ✅ EXACT | `Action_ReadDefender` | QB | `10` | `10` | 87 | START | 87 | 102 |
| ✅ EXACT | `Action_PullBall` | QB | `10` | `10` | 103 | START | 103 | 115 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 144 | START | 144 | 151 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_None` | 86 | 86 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 87 | 102 | 16 | inferred_complete_timeline |
| `Action_PullBall` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 116 | 143 | 28 | inferred_complete_timeline |
| `Action_ThrowPass` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_None` | 152 | 191 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 95 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 232 | 153 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 239 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 117 | 38 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 177 | 26 | inferred_complete_timeline |
| `Action_None` | 182 | 193 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 122 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 113 | 33 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 207 | 29 | inferred_complete_timeline |
| `Action_None` | 212 | 222 | 11 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 112 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 151 | 14 | inferred_complete_timeline |
| `Action_None` | 152 | 174 | 23 | inferred_complete_timeline |
| `Action_None` | 182 | 204 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 104 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 109 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 114 | 35 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 107 | 28 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 90 | 11 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 99 | 111 | 13 | inferred_complete_timeline |
| `Action_None` | 123 | 129 | 7 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 157 | 163 | 7 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 239 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 239 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 114 | 35 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 122 | 43 | inferred_complete_timeline |
| `Action_None` | 136 | 140 | 5 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 194 | 45 | inferred_complete_timeline |
| `Action_None` | 221 | 230 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 209 | 130 | inferred_complete_timeline |
| `Action_None` | 211 | 230 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 239 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 117 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 151 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 105–122 | 18 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 139–239 | 55 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 152–239 | 88 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 153–188 | 33 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 159–239 | 81 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 166–239 | 63 | 5 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 172–239 | 68 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 175–239 | 31 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 176–239 | 30 | 6 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 192–239 | 46 | 3 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 200–203 | 4 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 219–234 | 7 | 3 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 225–234 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 81 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [80-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-232] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-194] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-230] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-207] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-107] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 80, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [80-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-193] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-95] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-95] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-112] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-174] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-204] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-122] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-155] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-218] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-239] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-239] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-194] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-212] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '34' has 1 frames without a visible bounding box.
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

</details>