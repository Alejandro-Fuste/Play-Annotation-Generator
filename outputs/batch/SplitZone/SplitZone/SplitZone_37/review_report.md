# Play-Annotation-Generator Annotation Review — SplitZone_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_37`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `20` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 58 | START | 58 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `16` | 61 | START | 61 | 155 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `17` | 61 | START | 61 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `18` | 61 | START | 73 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `19` | 61 | START | 61 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `14` | `14` | 63 | START | 63 | 101 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 72 | END | 58 | 72 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 79 | START | 79 | 104 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `20` | `20` | 105 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 155 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_None` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 79 | 104 | 26 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_SplitBlock` | 63 | 101 | 39 | inferred_complete_timeline |
| `Action_SplitBlock` | 105 | 155 | 51 | inferred_complete_timeline |
| `Action_None` | 156 | 178 | 23 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 103 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 155 | 50 | inferred_complete_timeline |
| `Action_None` | 156 | 220 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 93 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 127 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 141 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 155 | 13 | inferred_complete_timeline |
| `Action_None` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 82 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 155 | 95 | inferred_complete_timeline |
| `Action_None` | 156 | 182 | 27 | inferred_complete_timeline |
| `Action_None` | 184 | 221 | 38 | inferred_complete_timeline |
| `Action_None` | 223 | 239 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 91 | 34 | inferred_complete_timeline |
| `Action_None` | 123 | 239 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 95 | 38 | inferred_complete_timeline |
| `Action_None` | 97 | 167 | 71 | inferred_complete_timeline |
| `Action_None` | 169 | 212 | 44 | inferred_complete_timeline |
| `Action_None` | 216 | 239 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 95 | 38 | inferred_complete_timeline |
| `Action_None` | 97 | 101 | 5 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_None` | 118 | 169 | 52 | inferred_complete_timeline |
| `Action_None` | 174 | 181 | 8 | inferred_complete_timeline |
| `Action_None` | 186 | 224 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 135 | 78 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 206 | 23 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 181 | 124 | inferred_complete_timeline |
| `Action_None` | 184 | 238 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 154 | 97 | inferred_complete_timeline |
| `Action_None` | 158 | 167 | 10 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 239 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 179 | 122 | inferred_complete_timeline |
| `Action_None` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 208 | 15 | inferred_complete_timeline |
| `Action_None` | 210 | 215 | 6 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 59–168 | 16 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 99–124 | 23 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 141–205 | 47 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 168–226 | 54 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 168–179 | 8 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 186–239 | 54 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 203–239 | 33 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `20` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 95 frames exceeds threshold 90 frames [start=61, end=155].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 95 frames exceeds threshold 90 frames [start=61, end=155].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [58–72], lower_priority='Action_ZoneBlock' annotated_start=61, effective_Action_ZoneBlock_start=73.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 95 frames exceeds threshold 90 frames [start=61, end=155].
- ⚠️ Segment 'Action_BallCarry' for track '20' has invalid range: start=105, end=78. Clamping end to start.
- ⚠️ Action 'Action_None' range [58-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-95] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [63-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [105-155] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-115] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-169] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-224] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-220] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-68] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '27' has 1 frames without a visible bounding box.
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

</details>