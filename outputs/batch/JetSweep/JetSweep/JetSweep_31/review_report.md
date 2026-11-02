# Play-Annotation-Generator Annotation Review — JetSweep_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_31`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 55
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 28
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Toss` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `3` | `2` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `18` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `22` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_JetMotion` | WR | `3` | `2` | 13 | START | 13 | 74 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 48 | START | 48 | 61 |
| ✅ EXACT | `Action_LeadBlock` | RB | `4` | `3` | 49 | START | 49 | 115 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `13` | 49 | START | 49 | 115 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `17` | 49 | START | 49 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 49 | START | 49 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 49 | START | 62 | 115 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 49 | START | 49 | 115 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 61 | END | 48 | 61 |
| ✅ EXACT | `Action_Toss` | QB | `17` | `16` | 68 | START | 68 | 74 |
| ✅ EXACT | `Action_BallCarry` | WR | `3` | `2` | 75 | START | 75 | 239 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `14` | `13` | 115 | BOUNDARY | 49 | 115 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `18` | `17` | 115 | BOUNDARY | 49 | 115 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `20` | `19` | 115 | BOUNDARY | 49 | 115 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `21` | `20` | 115 | BOUNDARY | 62 | 115 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `22` | `21` | 115 | BOUNDARY | 49 | 115 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 61 | 14 | inferred_complete_timeline |
| `Action_None` | 62 | 67 | 6 | inferred_complete_timeline |
| `Action_Toss` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_None` | 75 | 181 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_LeadBlock` | 49 | 115 | 67 | inferred_complete_timeline |
| `Action_None` | 116 | 171 | 56 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 239 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 133 | 86 | inferred_complete_timeline |
| `Action_None` | 138 | 239 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_JetMotion` | 13 | 74 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 75 | 239 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 115 | 67 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 115 | 67 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 61 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 115 | 54 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 115 | 67 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 115 | 67 | inferred_complete_timeline |
| `Action_None` | 116 | 147 | 32 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 85 | 38 | inferred_complete_timeline |
| `Action_None` | 94 | 239 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 95 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 72 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 100 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 197 | 150 | inferred_complete_timeline |
| `Action_None` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 172 | 125 | inferred_complete_timeline |
| `Action_None` | 175 | 189 | 15 | inferred_complete_timeline |
| `Action_None` | 192 | 204 | 13 | inferred_complete_timeline |
| `Action_None` | 206 | 239 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 157 | 110 | inferred_complete_timeline |
| `Action_None` | 160 | 175 | 16 | inferred_complete_timeline |
| `Action_None` | 177 | 220 | 44 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `27` | Position_Unknown | Team_Unknown | 68–93 | 8 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 70–72 | 3 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 93–239 | 147 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 100–101 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 113–140 | 17 | 4 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 155–239 | 85 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 156–176 | 17 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 160–239 | 80 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 186–239 | 50 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 33 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [48–61], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=62.
- ⚠️ Action 'Action_None' range [48-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-95] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-189] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-85] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-115] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-175] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-220] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-169] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '31' has 1 frames without a visible bounding box.
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