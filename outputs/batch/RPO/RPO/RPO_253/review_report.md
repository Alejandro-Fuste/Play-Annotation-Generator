# Play-Annotation-Generator Annotation Review — RPO_253

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_253`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `1` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | RT | offense | `6` | `6` |
| ❌ MISSING SEGMENT | `Action_PullBall` | RT | offense | `6` | `6` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RT | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `10` | 38 | START | 38 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 38 | START | 38 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 38 | START | 38 | 101 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `6` | 38 | START | 38 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `7` | 38 | START | 38 | 49 |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | RT | `6` | `6` | 72 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PullBall` | RT | `6` | `6` | 106 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RT | `6` | `6` | 141 | START | N/A | N/A |

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
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 117 | 81 | inferred_complete_timeline |
| `Action_None` | 119 | 135 | 17 | inferred_complete_timeline |
| `Action_None` | 138 | 180 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 53 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 165 | 129 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 134 | 98 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 140 | 157 | 18 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 150 | 114 | inferred_complete_timeline |
| `Action_None` | 153 | 166 | 14 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 89 | 53 | inferred_complete_timeline |
| `Action_None` | 92 | 109 | 18 | inferred_complete_timeline |
| `Action_None` | 123 | 145 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 49 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 89 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 135 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 101 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 121 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 135 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 145 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 153 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 47 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 62 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 75 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 60 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 88 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 117 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 145 | 20 | inferred_complete_timeline |
| `Action_None` | 146 | 146 | 1 | inferred_complete_timeline |
| `Action_None` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 164 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 62 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 135 | 99 | inferred_complete_timeline |
| `Action_None` | 160 | 168 | 9 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 36 | 14 | inferred_complete_timeline |
| `Action_None` | 37 | 50 | 14 | inferred_complete_timeline |
| `Action_None` | 52 | 80 | 29 | inferred_complete_timeline |
| `Action_None` | 82 | 116 | 35 | inferred_complete_timeline |
| `Action_None` | 120 | 147 | 28 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 129 | 93 | inferred_complete_timeline |
| `Action_None` | 161 | 165 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 45 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 135 | 99 | inferred_complete_timeline |
| `Action_None` | 138 | 156 | 19 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 146 | 110 | inferred_complete_timeline |
| `Action_None` | 151 | 180 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 72 | 36 | inferred_complete_timeline |
| `Action_None` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 154 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 180 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 131 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 180 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 180 | 144 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 64–141 | 69 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 73–169 | 73 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 73–117 | 45 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 124–160 | 26 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 133–180 | 48 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 162–164 | 3 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 176–180 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ❌ Missing segment for action `Action_ReadDefender` on target `6` (RT)
- ❌ Missing segment for action `Action_PullBall` on target `6` (RT)
- ❌ Missing segment for action `Action_ThrowPass` on target `6` (RT)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ReadDefender' for track '6' has invalid range: start=72, end=62. Clamping end to start.
- ⚠️ Segment 'Action_PullBall' for track '6' has invalid range: start=106, end=62. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '6' has invalid range: start=141, end=62. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 98 frames exceeds threshold 90 frames [start=38, end=135].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 108 frames exceeds threshold 90 frames [start=38, end=145].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 108 frames exceeds threshold 90 frames [start=38, end=145].
- ⚠️ Action 'Action_None' range [37-134] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-165] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-166] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-89] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-62] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-89] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-135] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-156] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 146, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [146-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-135] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-146] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-129] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-36] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-75] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-135] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-78] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-99] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-135] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-86] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-117] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-135] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '29' has 2 frames without a visible bounding box.
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