# Play-Annotation-Generator Annotation Review — BootPass_106

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_106`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 4
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | Team_Unknown | `19` | `19` |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `25` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 11 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 49 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 11 | START | 11 | 55 |
| ✅ EXACT | `Action_RunBlock` | RG | `13` | `13` | 50 | START | 50 | 210 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `14` | `14` | 50 | START | 56 | 143 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LG | `15` | `15` | 50 | START | N/A | N/A |
| ✅ EXACT | `Action_RunBlock` | RT | `2` | `2` | 50 | START | 50 | 210 |
| ✅ EXACT | `Action_RunBlock` | LT | `4` | `4` | 50 | START | 50 | 141 |
| ❌ MISSING SEGMENT | `Action_FakeHandoff` | Position_Unknown | `19` | `19` | 55 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `19` | `19` | 55 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | `19` | `19` | 89 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | `19` | `19` | 131 | START | 141 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | Position_Unknown | `25` | `22` | 166 | START | 166 | 189 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 164 | 154 | inferred_complete_timeline |
| `Action_None` | 168 | 170 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 167 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 141 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 11–15
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 15 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 55 | 45 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 143 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 49 | 45 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 210 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 210 | 161 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 92 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 190 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 201 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_None` | 15 | 133 | 119 | inferred_complete_timeline |
| `Action_None` | 135 | 206 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_None` | 181 | 210 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 70 | 60 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 23 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–168 | 169 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 40–188 | 147 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 59–210 | 149 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 127–138 | 12 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 141–208 | 63 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 151–210 | 58 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 154–210 | 50 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 155–206 | 48 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 163–170 | 8 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 172–203 | 25 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 173–201 | 27 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 196–210 | 15 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 203–208 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `14` (C): Annotated start 50 != Inferred start 56
- ❌ Missing segment for action `Action_RunBlock` on target `15` (LG)
- ❌ Missing segment for action `Action_FakeHandoff` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_SnapReceive` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_BootAway` on target `19` (Position_Unknown)
- ⚠️ `Action_ThrowPass` for actor_track_id `19` (Position_Unknown): Annotated start 131 != Inferred start 141
- ⚠️ Ambiguous match for action `Action_SecureCatch` and target `25` (2 segments found)

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [11–55], lower_priority='Action_RunBlock' annotated_start=50, effective_Action_RunBlock_start=56.
- ⚠️ Segment 'Action_RunBlock' for track '15' has invalid range: start=50, end=15. Clamping end to start.
- ⚠️ Overlapping action conflict at frame 55 for track '19': 'Action_SnapReceive' vs 'Action_FakeHandoff'. Overriding with 'Action_FakeHandoff'.
- ⚠️ Segment 'Action_FakeHandoff' for track '19' has invalid range: start=141, end=98. Clamping end to start.
- ⚠️ Segment 'Action_BootAway' for track '19' has invalid range: start=141, end=128. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '19' has invalid range: start=141, end=139. Clamping end to start.
- ⚠️ Action 'Action_None' range [11-70] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-141] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-168] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-23] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-12] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-181] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [166-189] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-206] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-194] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-197] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>