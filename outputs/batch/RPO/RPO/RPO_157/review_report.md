# Play-Annotation-Generator Annotation Review — RPO_157

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_157`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `5` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `5` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_RunBlock` | LT | `14` | `14` | 47 | START | 47 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `15` | `15` | 47 | START | 47 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `18` | `18` | 47 | START | 47 | 56 |
| ✅ EXACT | `Action_RunBlock` | LG | `20` | `20` | 47 | START | 47 | 92 |
| ✅ EXACT | `Action_RunBlock` | RT | `21` | `21` | 47 | START | 47 | 92 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `12` | 58 | START | 58 | 70 |
| ✅ EXACT | `Action_PullBall` | QB | `12` | `12` | 71 | START | 71 | 77 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 87 | START | 87 | 92 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_ReadDefender` | 58 | 70 | 13 | inferred_complete_timeline |
| `Action_PullBall` | 71 | 77 | 7 | inferred_complete_timeline |
| `Action_None` | 78 | 86 | 9 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 92 | 6 | inferred_complete_timeline |
| `Action_None` | 93 | 180 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 140 | 95 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 180 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 67 | 22 | inferred_complete_timeline |
| `Action_None` | 69 | 146 | 78 | inferred_complete_timeline |
| `Action_None` | 149 | 153 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 144 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 108 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 92 | 46 | inferred_complete_timeline |
| `Action_None` | 93 | 159 | 67 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 92 | 46 | inferred_complete_timeline |
| `Action_None` | 93 | 161 | 69 | inferred_complete_timeline |
| `Action_None` | 163 | 180 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 56 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 60 | 92 | 33 | inferred_complete_timeline |
| `Action_None` | 93 | 140 | 48 | inferred_complete_timeline |
| `Action_None` | 146 | 162 | 17 | inferred_complete_timeline |
| `Action_None` | 164 | 180 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 62 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 64 | 68 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 92 | 46 | inferred_complete_timeline |
| `Action_None` | 93 | 96 | 4 | inferred_complete_timeline |
| `Action_None` | 98 | 180 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 139 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 112 | 67 | inferred_complete_timeline |
| `Action_None` | 115 | 119 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 138 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 161 | 116 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 140 | 95 | inferred_complete_timeline |
| `Action_None` | 144 | 180 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 140 | 95 | inferred_complete_timeline |
| `Action_None` | 145 | 148 | 4 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 169 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 143 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 78–151 | 60 | 5 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 89–180 | 69 | 6 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 140–180 | 41 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 151–155 | 5 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 152–159 | 8 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 160–180 | 21 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 163–168 | 6 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 165–180 | 15 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 165–168 | 4 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 166–169 | 4 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 170–178 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 69 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [46-139] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-108] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-56] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-140] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-143] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-161] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-159] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [64-68] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-112] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-140] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [60-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-161] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-92] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-180] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-94] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-151] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-125] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '33' has 1 frames without a visible bounding box.
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