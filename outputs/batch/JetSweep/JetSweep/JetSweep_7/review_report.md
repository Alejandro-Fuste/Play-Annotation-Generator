# Play-Annotation-Generator Annotation Review — JetSweep_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_7`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 4
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `21` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `24` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `16` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `17` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `18` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `21` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 13 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 120 |
| ✅ EXACT | `Action_JetMotion` | WR | `3` | `2` | 90 | START | 90 | 148 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 121 | START | 121 | 137 |
| ✅ EXACT | `Action_LeadBlock` | TE | `12` | `11` | 123 | START | 123 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 123 | START | 148 | 149 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `17` | `16` | 123 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `18` | `17` | 123 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `21` | `18` | 123 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 137 | END | 121 | 137 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 141 | START | 141 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `3` | `2` | 149 | START | 149 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `24` | `20` | 161 | START | 161 | 189 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `16` | `15` | 200 | BOUNDARY | 154 | 200 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `17` | `16` | 200 | BOUNDARY | N/A | 200 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `18` | `17` | 200 | BOUNDARY | N/A | 200 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `21` | `18` | 200 | BOUNDARY | N/A | 200 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_SnapReceive` | 121 | 137 | 17 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_Toss` | 141 | 148 | 8 | inferred_complete_timeline |
| `Action_None` | 149 | 240 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 169 | 49 | inferred_complete_timeline |
| `Action_None` | 173 | 246 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 195 | 75 | inferred_complete_timeline |
| `Action_None` | 205 | 225 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_JetMotion` | 90 | 148 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 149 | 224 | 76 | inferred_complete_timeline |
| `Action_BallCarry` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 271 | 282 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 284 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_LeadBlock` | 123 | 200 | 78 | inferred_complete_timeline |
| `Action_None` | 201 | 221 | 21 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 13–20
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 20 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_BallSnap` | 121 | 137 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 200 | 47 | inferred_complete_timeline |
| `Action_None` | 201 | 284 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–18
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 18 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–17
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 17 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 44 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 62 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 15–19
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 19 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 225 | 105 | inferred_complete_timeline |
| `Action_None` | 227 | 286 | 60 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 196 | 76 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 202 | 299 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 212 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 187 | 67 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 240 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 276 | 156 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 278 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `24` | Position_Unknown | Team_Unknown | 151–299 | 125 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 151–299 | 142 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 153–266 | 114 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 153–278 | 126 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 156–299 | 144 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 157–254 | 94 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 160–299 | 139 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 163–299 | 112 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 233–287 | 55 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 233–274 | 39 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 239–241 | 3 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 245–299 | 17 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 269–293 | 18 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `17` (RG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `18` (RT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (LT)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `24` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 15: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [121–137], lower_priority='Action_ZoneBlock' annotated_start=123, effective_Action_ZoneBlock_start=138.
- ⚠️ Segment 'Action_ZoneBlock' for track '16' has invalid range: start=123, end=18. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '17' has invalid range: start=123, end=17. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '18' has invalid range: start=123, end=20. Clamping end to start.
- ⚠️ Action 'Action_None' range [121-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-246] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-225] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [149-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [260-261] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-282] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-276] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-240] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-196] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-212] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-278] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-221] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-225] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-286] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-44] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [121-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-284] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [161-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-266] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-278] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-236] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-287] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-250] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-264] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-254] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-278] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-293] for track '33' has 1 frames without a visible bounding box.
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

</details>