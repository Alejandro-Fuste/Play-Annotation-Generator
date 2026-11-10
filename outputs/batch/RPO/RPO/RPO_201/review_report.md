# Play-Annotation-Generator Annotation Review — RPO_201

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_201`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunOutRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `0` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 45 | START | 45 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 45 | START | 45 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 45 | START | 45 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 45 | START | 45 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `9` | 45 | START | 47 | 92 |
| ✅ EXACT | `Action_ReadDefender` | QB | `21` | `21` | 48 | START | 48 | 62 |
| ✅ EXACT | `Action_PullBall` | QB | `21` | `21` | 63 | START | 63 | 72 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 114 | START | 114 | 121 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 48 | 62 | 15 | inferred_complete_timeline |
| `Action_PullBall` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_None` | 73 | 113 | 41 | inferred_complete_timeline |
| `Action_ThrowPass` | 114 | 121 | 8 | inferred_complete_timeline |
| `Action_None` | 122 | 195 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 90 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 53 | 10 | inferred_complete_timeline |
| `Action_None` | 56 | 189 | 134 | inferred_complete_timeline |
| `Action_None` | 191 | 204 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 49 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 121 | 71 | inferred_complete_timeline |
| `Action_None` | 122 | 183 | 62 | inferred_complete_timeline |
| `Action_None` | 186 | 191 | 6 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 121 | 26 | inferred_complete_timeline |
| `Action_None` | 122 | 210 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 92 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 112 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 144 | 148 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 49 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 54 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 121 | 77 | inferred_complete_timeline |
| `Action_None` | 122 | 210 | 89 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 199 | 156 | inferred_complete_timeline |
| `Action_None` | 201 | 210 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 55 | 12 | inferred_complete_timeline |
| `Action_None` | 57 | 83 | 27 | inferred_complete_timeline |
| `Action_None` | 85 | 148 | 64 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 105 | 62 | inferred_complete_timeline |
| `Action_None` | 107 | 210 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 132 | 89 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 163 | 22 | inferred_complete_timeline |
| `Action_None` | 165 | 210 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 202 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 178 | 135 | inferred_complete_timeline |
| `Action_None` | 181 | 206 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 46–70 | 12 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 55–57 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 67–152 | 47 | 6 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 88–89 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 88–210 | 105 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 88–140 | 19 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 108–109 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 108–202 | 90 | 4 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 110–169 | 6 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 117–118 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 147–210 | 50 | 4 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 149–152 | 4 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 155–210 | 52 | 2 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 190–209 | 20 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 198–210 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 90 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [44-53] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-204] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 44, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [44-44] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-112] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-199] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-49] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-51] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-94] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-156] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-173] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-126] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-182] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-188] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-176] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-209] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '39' has 1 frames without a visible bounding box.
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

</details>