# Play-Annotation-Generator Annotation Review — JetSweep_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_82`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 62
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `6` | `5` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 99 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `6` | `5` | 71 | START | 71 | 135 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 100 | START | 100 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `20` | `19` | 101 | START | 101 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 101 | START | 119 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `16` | 101 | START | 101 | 193 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `19` | `18` | 101 | START | 101 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 101 | START | 101 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 101 | START | 101 | 144 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 118 | END | 100 | 118 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 121 | START | 121 | 135 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `21` | `20` | 132 | START | 132 | 193 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `6` | `5` | 136 | START | 136 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 193 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_SnapReceive` | 100 | 118 | 19 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_Toss` | 121 | 135 | 15 | inferred_complete_timeline |
| `Action_None` | 136 | 218 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 235 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_JetMotion` | 71 | 135 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 269 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_LeadBlock` | 101 | 139 | 39 | inferred_complete_timeline |
| `Action_LeadBlock` | 141 | 193 | 53 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 193 | 93 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 193 | 93 | inferred_complete_timeline |
| `Action_None` | 194 | 252 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_BallSnap` | 100 | 118 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 131 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 193 | 61 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 144 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 193 | 47 | inferred_complete_timeline |
| `Action_None` | 194 | 249 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 131 | 31 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 132 | 193 | 62 | inferred_complete_timeline |
| `Action_None` | 194 | 249 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 139 | 40 | inferred_complete_timeline |
| `Action_None` | 147 | 241 | 95 | inferred_complete_timeline |
| `Action_None` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 147 | 48 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 269 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 169 | 70 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 250 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 267 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 247 | 148 | inferred_complete_timeline |
| `Action_None` | 251 | 256 | 6 | inferred_complete_timeline |
| `Action_None` | 264 | 268 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–55 | 39 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 80–83 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 120–127 | 6 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 208–264 | 43 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 210–214 | 5 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 261–265 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 93 frames exceeds threshold 90 frames [start=101, end=193].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [100–118], lower_priority='Action_ZoneBlock' annotated_start=101, effective_Action_ZoneBlock_start=119.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (LG) duration 93 frames exceeds threshold 90 frames [start=101, end=193].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 93 frames exceeds threshold 90 frames [start=101, end=193].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '19' (TE) duration 93 frames exceeds threshold 90 frames [start=101, end=193].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 93 frames exceeds threshold 90 frames [start=101, end=193].
- ⚠️ Action 'Action_None' range [100-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-235] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-247] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [119-131] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-193] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-139] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-241] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-147] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-169] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-250] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-252] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [101-139] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-249] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-144] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-249] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-34] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-41] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-83] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-264] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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