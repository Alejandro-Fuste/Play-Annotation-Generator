# Play-Annotation-Generator Annotation Review — RPO_107

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_107`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `2` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_ReadDefender` | QB | `16` | `16` | 27 | START | 27 | 51 |
| ✅ EXACT | `Action_PullBall` | QB | `16` | `16` | 52 | START | 52 | 58 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 74 | START | 74 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 77 | START | 77 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | C | `18` | `18` | 77 | START | 77 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `19` | 77 | START | 77 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `20` | 77 | START | 77 | 82 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `21` | `21` | 77 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ReadDefender` | 27 | 51 | 25 | inferred_complete_timeline |
| `Action_PullBall` | 52 | 58 | 7 | inferred_complete_timeline |
| `Action_None` | 59 | 73 | 15 | inferred_complete_timeline |
| `Action_ThrowPass` | 74 | 82 | 9 | inferred_complete_timeline |
| `Action_None` | 83 | 139 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 75 | 23 | inferred_complete_timeline |
| `Action_None` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 269 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 269 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 221 | 146 | inferred_complete_timeline |
| `Action_None` | 227 | 238 | 12 | inferred_complete_timeline |
| `Action_None` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 197 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_None` | 83 | 92 | 10 | inferred_complete_timeline |
| `Action_None` | 100 | 187 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 40 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 69 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 74 | 29 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_None` | 83 | 140 | 58 | inferred_complete_timeline |
| `Action_None` | 143 | 205 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_None` | 83 | 165 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_None` | 83 | 205 | 123 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_None` | 76 | 100 | 25 | inferred_complete_timeline |
| `Action_None` | 106 | 269 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 119 | 44 | inferred_complete_timeline |
| `Action_None` | 121 | 137 | 17 | inferred_complete_timeline |
| `Action_None` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_None` | 155 | 269 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 40 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 134 | 23 | inferred_complete_timeline |
| `Action_None` | 136 | 214 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 79 | 4 | inferred_complete_timeline |
| `Action_None` | 87 | 157 | 71 | inferred_complete_timeline |
| `Action_None` | 161 | 269 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 87 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 269 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 269 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 94 | 19 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 110 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 141 | 66 | inferred_complete_timeline |
| `Action_None` | 143 | 251 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 100 | 25 | inferred_complete_timeline |
| `Action_None` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_None` | 111 | 269 | 159 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 54–228 | 169 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 100–146 | 47 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 115–252 | 137 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 121–123 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 130–222 | 93 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 138–246 | 107 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 152–223 | 41 | 7 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 157–163 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (LG)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=77, end=69. Clamping end to start.
- ⚠️ Action 'Action_None' range [76-221] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-238] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-157] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-141] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-251] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-43] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-100] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-269] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-100] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-214] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-74] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-165] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-228] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-222] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-246] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '29' has 2 frames without a visible bounding box.
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

</details>