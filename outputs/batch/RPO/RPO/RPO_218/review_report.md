# Play-Annotation-Generator Annotation Review — RPO_218

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_218`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSeamRoute` | actor_track_id `16` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | TE3 | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 31 | START | 31 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `12` | 31 | START | 31 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 31 | START | 31 | 33 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 31 | START | 31 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `9` | 31 | START | 31 | 41 |
| ✅ EXACT | `Action_ReadDefender` | QB | `4` | `4` | 35 | START | 35 | 50 |
| ✅ EXACT | `Action_PullBall` | QB | `4` | `4` | 51 | START | 51 | 59 |
| ✅ EXACT | `Action_ThrowPass` | TE3 | `16` | `16` | 83 | START | 83 | 90 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 34 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 35 | 50 | 16 | inferred_complete_timeline |
| `Action_PullBall` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_None` | 60 | 210 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 95 | 66 | inferred_complete_timeline |
| `Action_None` | 103 | 210 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 32 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 29 | 7 | inferred_complete_timeline |
| `Action_None` | 30 | 31 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_None` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_None` | 49 | 82 | 34 | inferred_complete_timeline |
| `Action_ThrowPass` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_None` | 91 | 210 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 39 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 67 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 62 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 43 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 41 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 74 | 29 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 34 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 56 | 27 | inferred_complete_timeline |
| `Action_None` | 76 | 93 | 18 | inferred_complete_timeline |
| `Action_None` | 98 | 178 | 81 | inferred_complete_timeline |
| `Action_None` | 185 | 193 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 68 | 39 | inferred_complete_timeline |
| `Action_None` | 72 | 86 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 46 | 17 | inferred_complete_timeline |
| `Action_None` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_None` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 126 | 4 | inferred_complete_timeline |
| `Action_None` | 133 | 154 | 22 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |
| `Action_None` | 164 | 176 | 13 | inferred_complete_timeline |
| `Action_None` | 178 | 210 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 65 | 36 | inferred_complete_timeline |
| `Action_None` | 69 | 90 | 22 | inferred_complete_timeline |
| `Action_None` | 93 | 112 | 20 | inferred_complete_timeline |
| `Action_None` | 115 | 129 | 15 | inferred_complete_timeline |
| `Action_None` | 132 | 210 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 59 | 30 | inferred_complete_timeline |
| `Action_None` | 63 | 71 | 9 | inferred_complete_timeline |
| `Action_None` | 77 | 97 | 21 | inferred_complete_timeline |
| `Action_None` | 100 | 120 | 21 | inferred_complete_timeline |
| `Action_None` | 122 | 176 | 55 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 204 | 16 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 210 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 210 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 59 | 30 | inferred_complete_timeline |
| `Action_None` | 62 | 102 | 41 | inferred_complete_timeline |
| `Action_None` | 104 | 210 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 149 | 120 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 70 | 41 | inferred_complete_timeline |
| `Action_None` | 72 | 190 | 119 | inferred_complete_timeline |
| `Action_None` | 192 | 200 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | Position_Unknown | Team_Unknown | 108–158 | 42 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 110–210 | 98 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 126–210 | 85 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 127–210 | 84 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 134–199 | 14 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 166–210 | 44 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 167–171 | 5 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 167–201 | 16 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 169–210 | 20 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 86 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [30-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-56] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-178] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-46] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-56] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-154] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-176] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-65] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-112] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-129] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '6' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-34] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-41] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-74] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-200] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-68] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-86] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-38] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-210] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-59] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-97] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-120] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-204] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-31] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-149] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-210] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-179] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '30' has 1 frames without a visible bounding box.
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