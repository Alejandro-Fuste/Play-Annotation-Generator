# Play-Annotation-Generator Annotation Review — JetSweep_179

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_179`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 67
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
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `7` | `6` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `23` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 74 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `7` | `6` | 43 | START | 43 | 96 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 73 | START | 73 | 86 |
| ✅ EXACT | `Action_LeadBlock` | TE | `6` | `5` | 75 | START | 75 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 75 | START | 87 | 95 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `16` | 75 | START | 75 | 148 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `19` | 75 | START | 75 | 148 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 75 | START | 75 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `8` | 75 | START | 75 | 148 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 86 | END | 73 | 86 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 94 | START | 94 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `7` | `6` | 97 | START | 97 | 265 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 148 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 86 | 14 | inferred_complete_timeline |
| `Action_None` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_Toss` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 299 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 150 | 78 | inferred_complete_timeline |
| `Action_None` | 154 | 170 | 17 | inferred_complete_timeline |
| `Action_None` | 172 | 299 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 299 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_JetMotion` | 43 | 96 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 265 | 169 | inferred_complete_timeline |
| `Action_BallCarry` | 275 | 279 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 299 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_LeadBlock` | 75 | 148 | 74 | inferred_complete_timeline |
| `Action_None` | 149 | 299 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 148 | 74 | inferred_complete_timeline |
| `Action_None` | 149 | 299 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 148 | 74 | inferred_complete_timeline |
| `Action_None` | 149 | 149 | 1 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_BallSnap` | 73 | 86 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 95 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 113 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 148 | 74 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |
| `Action_None` | 275 | 299 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 148 | 74 | inferred_complete_timeline |
| `Action_None` | 149 | 299 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 152 | 80 | inferred_complete_timeline |
| `Action_None` | 160 | 170 | 11 | inferred_complete_timeline |
| `Action_None` | 172 | 299 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 173 | 101 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 218 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 132 | 60 | inferred_complete_timeline |
| `Action_None` | 136 | 149 | 14 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 151 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 299 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 240 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 129 | 57 | inferred_complete_timeline |
| `Action_None` | 132 | 140 | 9 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 152 | 6 | inferred_complete_timeline |
| `Action_None` | 159 | 299 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 299 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 299 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 289 | 217 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–87 | 88 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 100–299 | 191 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 103–144 | 20 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 141–204 | 47 | 5 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 176–299 | 124 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 193–299 | 107 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 230–299 | 48 | 7 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 260–299 | 40 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 279–299 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [73–86], lower_priority='Action_ZoneBlock' annotated_start=75, effective_Action_ZoneBlock_start=87.
- ⚠️ Action 'Action_None' range [73-87] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-173] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-265] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [275-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-151] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-152] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-149] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 149, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [149-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-289] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-218] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-150] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-163] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-195] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-299] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-241] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-284] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>