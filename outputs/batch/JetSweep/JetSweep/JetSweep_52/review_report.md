# Play-Annotation-Generator Annotation Review — JetSweep_52

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_52`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `2` | `1` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SealBlock` | WR2 | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `2` | `1` | 62 | START | 62 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `21` | `20` | 82 | START | 82 | 86 |
| ✅ EXACT | `Action_LeadBlock` | TE | `7` | `6` | 84 | START | 84 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 84 | START | 84 | 101 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `14` | 84 | START | 84 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 84 | START | 92 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 84 | START | 84 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 84 | START | 84 | 115 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 91 | END | 82 | 91 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 104 | START | 104 | 114 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `2` | `1` | 115 | START | 115 | 260 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `21` | `20` | 116 | START | 116 | 158 |
| ✅ EXACT | `Action_SealBlock` | WR2 | `1` | `0` | 144 | START | 144 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 158 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_SnapReceive` | 82 | 91 | 10 | inferred_complete_timeline |
| `Action_None` | 92 | 103 | 12 | inferred_complete_timeline |
| `Action_Toss` | 104 | 114 | 11 | inferred_complete_timeline |
| `Action_None` | 115 | 189 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 165 | 84 | inferred_complete_timeline |
| `Action_None` | 172 | 216 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_JetMotion` | 62 | 114 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 115 | 260 | 146 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_SealBlock` | 144 | 269 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_LeadBlock` | 84 | 158 | 75 | inferred_complete_timeline |
| `Action_None` | 159 | 224 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 115 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 158 | 41 | inferred_complete_timeline |
| `Action_None` | 159 | 191 | 33 | inferred_complete_timeline |
| `Action_None` | 193 | 201 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 101 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 115 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 116 | 158 | 43 | inferred_complete_timeline |
| `Action_None` | 159 | 230 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 158 | 75 | inferred_complete_timeline |
| `Action_None` | 159 | 210 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 158 | 75 | inferred_complete_timeline |
| `Action_None` | 159 | 191 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 221 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 123 | 42 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 204 | 123 | inferred_complete_timeline |
| `Action_None` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 111 | 30 | inferred_complete_timeline |
| `Action_None` | 118 | 141 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 238 | 157 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 249 | 168 | inferred_complete_timeline |
| `Action_None` | 253 | 262 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 151 | 70 | inferred_complete_timeline |
| `Action_None` | 156 | 167 | 12 | inferred_complete_timeline |
| `Action_None` | 169 | 269 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–195 | 196 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 83–87 | 5 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 120–269 | 150 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 132–191 | 6 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 134–145 | 10 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 142–204 | 63 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 149–221 | 73 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 190–214 | 25 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 222–236 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [82–91], lower_priority='Action_ZoneBlock' annotated_start=84, effective_Action_ZoneBlock_start=92.
- ⚠️ Action 'Action_BallCarry' range [115-260] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-224] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-221] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-262] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [82-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-99] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '21' starts at frame 84, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [84-158] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-87] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-221] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-236] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>