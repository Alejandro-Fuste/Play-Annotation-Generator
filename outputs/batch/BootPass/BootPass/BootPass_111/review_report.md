# Play-Annotation-Generator Annotation Review — BootPass_111

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_111`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LG | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RT | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `16` | `16` |
| ✅ EXACT | `Action_FakeHandoff` | DE2 | defense | `16` | `16` |
| ✅ EXACT | `Action_BootAway` | DE2 | defense | `16` | `16` |
| ✅ EXACT | `Action_RunFlatRoute` | DT2 | defense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | DE2 | defense | `16` | `16` |
| ✅ EXACT | `Action_SecureCatch` | DT2 | defense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `17` | `17` | 15 | START | 15 | 22 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LG | `13` | `13` | 82 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RT | `15` | `15` | 82 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | `17` | `17` | 82 | START | N/A | N/A |
| ✅ EXACT | `Action_RunBlock` | LT | `18` | `18` | 82 | START | 82 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `21` | `21` | 82 | START | 82 | 197 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `16` | `16` | 82 | END | 15 | 82 |
| ✅ EXACT | `Action_FakeHandoff` | DE2 | `16` | `16` | 102 | START | 102 | 116 |
| ✅ EXACT | `Action_BootAway` | DE2 | `16` | `16` | 117 | START | 117 | 137 |
| ✅ EXACT | `Action_RunFlatRoute` | DT2 | `14` | `14` | 123 | START | 123 | 159 |
| ✅ EXACT | `Action_ThrowPass` | DE2 | `16` | `16` | 140 | START | 140 | 149 |
| ✅ EXACT | `Action_SecureCatch` | DT2 | `14` | `14` | 160 | START | 160 | 168 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 149 | 135 | inferred_complete_timeline |
| `Action_None` | 156 | 212 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 217 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 68 | 54 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_RunBlock` | 82 | 239 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 22 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 30 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 59 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 81 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 82 | 197 | 116 | inferred_complete_timeline |
| `Action_RunBlock` | 199 | 206 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 230 | 237 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 39 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 63 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 46 | 32 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_None` | 96 | 129 | 34 | inferred_complete_timeline |
| `Action_None` | 133 | 188 | 56 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 82 | 68 | inferred_complete_timeline |
| `Action_None` | 83 | 101 | 19 | inferred_complete_timeline |
| `Action_FakeHandoff` | 102 | 116 | 15 | inferred_complete_timeline |
| `Action_BootAway` | 117 | 137 | 21 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_ThrowPass` | 140 | 149 | 10 | inferred_complete_timeline |
| `Action_None` | 150 | 239 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 121 | 107 | inferred_complete_timeline |
| `Action_None` | 124 | 239 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 122 | 22 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 123 | 159 | 37 | inferred_complete_timeline |
| `Action_SecureCatch` | 160 | 168 | 9 | inferred_complete_timeline |
| `Action_None` | 169 | 239 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 193 | 179 | inferred_complete_timeline |
| `Action_None` | 203 | 237 | 35 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 125 | 111 | inferred_complete_timeline |
| `Action_None` | 135 | 194 | 60 | inferred_complete_timeline |
| `Action_None` | 197 | 206 | 10 | inferred_complete_timeline |
| `Action_None` | 208 | 217 | 10 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 192 | 178 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_None` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_None` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 217 | 203 | inferred_complete_timeline |
| `Action_None` | 224 | 234 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 56–239 | 180 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 89–96 | 7 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 91–239 | 149 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 120–124 | 5 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 127–239 | 113 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `17` (2 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `13` (LG)
- ❌ Missing segment for action `Action_RunBlock` on target `15` (RT)
- ❌ Missing segment for action `Action_RunBlock` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_RunBlock' for track '13' has invalid range: start=82, end=32. Clamping end to start.
- ⚠️ Segment 'Action_RunBlock' for track '15' has invalid range: start=82, end=63. Clamping end to start.
- ⚠️ Segment 'Action_RunBlock' for track '17' has invalid range: start=82, end=30. Clamping end to start.
- ⚠️ Action 'Action_None' range [15-193] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-217] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-212] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-217] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-234] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-206] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [15-22] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [24-30] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-68] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-59] for track '21' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [82-197] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [199-206] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [209-214] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [216-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [220-223] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [230-237] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-194] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '28' has 1 frames without a visible bounding box.
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