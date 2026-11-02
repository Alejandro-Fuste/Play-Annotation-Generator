# Play-Annotation-Generator Annotation Review — JetSweep_110

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_110`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 41
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `7` | `6` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `17` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `7` | `6` | 51 | START | 51 | 102 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 68 | START | 68 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `6` | `5` | 76 | START | 76 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `17` | 76 | START | 76 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 76 | START | 81 | 95 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `19` | 76 | START | 76 | 167 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 76 | START | 76 | 167 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 76 | START | 76 | 167 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 80 | END | 68 | 80 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 89 | START | 89 | 102 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `7` | `6` | 103 | START | 103 | 222 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 167 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_SnapReceive` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_None` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_Toss` | 89 | 102 | 14 | inferred_complete_timeline |
| `Action_None` | 103 | 239 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_LeadBlock` | 76 | 145 | 70 | inferred_complete_timeline |
| `Action_LeadBlock` | 148 | 152 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_JetMotion` | 51 | 102 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 222 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 205 | 138 | inferred_complete_timeline |
| `Action_None` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 167 | 92 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 167 | 92 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_BallSnap` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 167 | 53 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 113 | 38 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 167 | 92 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 195 | 128 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 206 | 215 | 10 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_None` | 230 | 232 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 211 | 144 | inferred_complete_timeline |
| `Action_None` | 216 | 232 | 17 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 116 | 49 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 222 | 155 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 188 | 121 | inferred_complete_timeline |
| `Action_None` | 190 | 239 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 125–239 | 103 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 132–239 | 108 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 152–155 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 199–202 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF1` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 26 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 92 frames exceeds threshold 90 frames [start=76, end=167].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 92 frames exceeds threshold 90 frames [start=76, end=167].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 92 frames exceeds threshold 90 frames [start=76, end=167].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [68–80], lower_priority='Action_ZoneBlock' annotated_start=76, effective_Action_ZoneBlock_start=81.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 92 frames exceeds threshold 90 frames [start=76, end=167].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 92 frames exceeds threshold 90 frames [start=76, end=167].
- ⚠️ Action 'Action_None' range [68-239] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [76-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [148-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-222] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-211] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-232] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-137] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>