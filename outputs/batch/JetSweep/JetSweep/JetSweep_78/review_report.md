# Play-Annotation-Generator Annotation Review — JetSweep_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_78`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SealBlock` | TE2 | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 65 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `5` | `4` | 29 | START | 29 | 87 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 65 | START | 65 | 77 |
| ✅ EXACT | `Action_LeadBlock` | RB | `4` | `3` | 66 | START | 66 | 135 |
| ✅ EXACT | `Action_SealBlock` | TE2 | `10` | `9` | 66 | START | 66 | 192 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `15` | 66 | START | 66 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 66 | START | 66 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 66 | START | 66 | 135 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `22` | `21` | 66 | START | 78 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `8` | 66 | START | 66 | 135 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 77 | END | 65 | 77 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 80 | START | 80 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `5` | `4` | 88 | START | 88 | 151 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 135 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_SnapReceive` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_Toss` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_None` | 88 | 175 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_LeadBlock` | 66 | 135 | 70 | inferred_complete_timeline |
| `Action_None` | 136 | 239 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 189 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_JetMotion` | 29 | 87 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 151 | 64 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 189 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_SealBlock` | 66 | 192 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 135 | 70 | inferred_complete_timeline |
| `Action_None` | 136 | 199 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 135 | 70 | inferred_complete_timeline |
| `Action_None` | 136 | 155 | 20 | inferred_complete_timeline |
| `Action_None` | 157 | 183 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_BallSnap` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 117 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 135 | 70 | inferred_complete_timeline |
| `Action_None` | 136 | 193 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 135 | 70 | inferred_complete_timeline |
| `Action_None` | 136 | 239 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 100 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 239 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 111 | 47 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 106 | 42 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 189 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 189 | 125 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |
| `Action_None` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 114 | 50 | inferred_complete_timeline |
| `Action_None` | 126 | 162 | 37 | inferred_complete_timeline |
| `Action_None` | 167 | 173 | 7 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 218 | 154 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 189 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 189 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 239 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–239 | 212 | 8 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 126–239 | 113 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 137–200 | 64 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 179–181 | 3 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 190–239 | 49 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 190–239 | 49 | 2 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 223–239 | 14 | 3 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 226–239 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (C): Annotated start 66 != Inferred start 78
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 158: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [65–77], lower_priority='Action_ZoneBlock' annotated_start=66, effective_Action_ZoneBlock_start=78.
- ⚠️ Action 'Action_None' range [65-100] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-189] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-151] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [154-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-96] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-151] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-189] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [66-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-239] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-189] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-239] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-200] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-239] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>