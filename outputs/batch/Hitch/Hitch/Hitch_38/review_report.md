# Play-Annotation-Generator Annotation Review — Hitch_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_38`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_RunHitchRoute` | WR2 | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | WR2 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 2 | START | 2 | 6 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 5 | START | 7 | 12 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `15` | `15` | 5 | START | 5 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 5 | START | 5 | 7 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 6 | END | 2 | 6 |
| ✅ EXACT | `Action_RunHitchRoute` | WR2 | `7` | `7` | 14 | START | 14 | 45 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `18` | `18` | 83 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | WR2 | `7` | `7` | 139 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 6 | 5 | inferred_complete_timeline |
| `Action_None` | 7 | 7 | 1 | inferred_complete_timeline |
| `Action_None` | 32 | 36 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 41 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 46 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 14 | 45 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 23 | 22 | inferred_complete_timeline |
| `Action_None` | 32 | 41 | 10 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 77 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 12 | 11 | inferred_complete_timeline |
| `Action_None` | 32 | 38 | 7 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 38 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 6 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 12 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 36 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 7 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 37 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 7 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 12 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 8 | 7 | inferred_complete_timeline |
| `Action_None` | 32 | 44 | 13 | inferred_complete_timeline |
| `Action_None` | 48 | 54 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 6 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 111 | 110 | inferred_complete_timeline |
| `Action_None` | 113 | 204 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 182 | 181 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 199 | 198 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 188 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 149 | 148 | inferred_complete_timeline |
| `Action_None` | 155 | 160 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 201 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 20–42 | 13 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 25–210 | 143 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 33–210 | 178 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 34–106 | 69 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 52–126 | 74 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 53–160 | 108 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 75–99 | 16 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 102–210 | 109 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 123–209 | 60 | 3 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 135–201 | 67 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 142–210 | 63 | 3 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 142–210 | 69 | 1 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 143–210 | 61 | 3 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 149–210 | 61 | 2 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 149–210 | 59 | 4 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 155–210 | 56 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 165–210 | 35 | 2 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 165–210 | 43 | 2 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 170–180 | 10 | 2 | Undefined position; Undefined team |
| `40` | `44` | Position_Unknown | Team_Unknown | 194–206 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `18` (QB)
- ❌ Missing segment for action `Action_BallCarry` on target `7` (WR2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '7' has invalid range: start=139, end=45. Clamping end to start.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [2–6], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=7.
- ⚠️ Segment 'Action_ThrowPass' for track '18' has invalid range: start=83, end=36. Clamping end to start.
- ⚠️ Action 'Action_None' range [2-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-41] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-46] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-204] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-188] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [14-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-182] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-41] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-77] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-12] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-12] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-6] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-8] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-44] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-54] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-7] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 7, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [7-7] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '19' starts at frame 5, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [5-7] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-42] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-26] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-82] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-201] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-176] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '40' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>