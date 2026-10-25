# Play-Annotation-Generator Annotation Review — BootPass_129

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_129`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 5
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `6` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | LG | offense | `17` | `17` |
| ⚠️ START CHANGED | `Action_RunBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | LG | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_FakeHandoff` | LG | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_BootAway` | LG | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | SAF1 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `6` | `Group` | 0 | START | 0 | 19 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | LG | `17` | `17` | 20 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_RunBlock` | RT | `10` | `10` | 49 | START | 58 | 71 |
| ✅ EXACT | `Action_RunBlock` | LT | `16` | `16` | 49 | START | 49 | 54 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LG | `17` | `17` | 49 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | LG | `17` | `17` | 49 | END | 20 | 23 |
| ❌ MISSING SEGMENT | `Action_FakeHandoff` | LG | `17` | `17` | 67 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BootAway` | LG | `17` | `17` | 85 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RT | `10` | `10` | 127 | START | N/A | N/A |
| ✅ EXACT | `Action_SecureCatch` | SAF1 | `2` | `2` | 157 | START | 157 | 169 |

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
- **Visible Frames:** 0–143
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 26 | 7 | inferred_complete_timeline |
| `Action_None` | 28 | 30 | 3 | inferred_complete_timeline |
| `Action_None` | 34 | 62 | 29 | inferred_complete_timeline |
| `Action_None` | 64 | 143 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 89 | 70 | inferred_complete_timeline |
| `Action_None` | 94 | 110 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 38 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 56 | 37 | inferred_complete_timeline |
| `Action_None` | 60 | 162 | 103 | inferred_complete_timeline |
| `Action_None` | 168 | 170 | 3 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 183 | 6 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 204 | 214 | 11 | inferred_complete_timeline |
| `Action_None` | 217 | 223 | 7 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 145 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_RunBlock` | 49 | 54 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 23 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_None` | 55 | 62 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 58 | 71 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 28 | 9 | inferred_complete_timeline |
| `Action_None` | 34 | 61 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 299 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 47 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 52 | 33 | inferred_complete_timeline |
| `Action_None` | 60 | 118 | 59 | inferred_complete_timeline |
| `Action_None` | 121 | 123 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 165 | 146 | inferred_complete_timeline |
| `Action_None` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_None` | 177 | 299 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 66 | 47 | inferred_complete_timeline |
| `Action_None` | 73 | 193 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 199 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 68 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_SecureCatch` | 157 | 169 | 13 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 299 | 280 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 2–178 | 113 | 9 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 14–25 | 9 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 24–162 | 108 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 35–178 | 94 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 49–109 | 50 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 55–155 | 98 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 72–101 | 24 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 88–103 | 16 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 105–143 | 38 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 116–186 | 52 | 7 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 116–152 | 37 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 136–143 | 8 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 149–175 | 27 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 152–299 | 143 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 154–216 | 63 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 209–299 | 88 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 237–299 | 38 | 3 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 243–299 | 52 | 4 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 259–299 | 41 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `17` (LG)
- ⚠️ `Action_RunBlock` for actor_track_id `10` (RT): Annotated start 49 != Inferred start 58
- ❌ Missing segment for action `Action_RunBlock` on target `17` (LG)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `17` (3 segments found)
- ❌ Missing segment for action `Action_FakeHandoff` on target `17` (LG)
- ❌ Missing segment for action `Action_BootAway` on target `17` (LG)
- ❌ Missing segment for action `Action_ThrowPass` on target `10` (RT)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '10' has invalid range: start=127, end=71. Clamping end to start.
- ⚠️ Overlapping action conflict at frame 49 for track '17': 'Action_RunBlock' vs 'Action_SnapReceive'. Overriding with 'Action_SnapReceive'.
- ⚠️ Segment 'Action_FakeHandoff' for track '17' has invalid range: start=67, end=62. Clamping end to start.
- ⚠️ Segment 'Action_BootAway' for track '17' has invalid range: start=85, end=62. Clamping end to start.
- ⚠️ Action 'Action_None' range [20-89] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-165] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-199] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-38] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-28] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [58-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-26] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-30] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-143] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-47] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-145] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-214] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [49-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [20-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [27-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [35-38] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-62] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-19] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-26] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-136] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-178] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-18] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-25] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-123] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-178] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-65] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-155] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-91] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-103] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-143] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-152] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-175] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-216] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-299] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-262] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-270] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '35' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>