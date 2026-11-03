# Play-Annotation-Generator Annotation Review — Slants0to10_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_45`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 11 | START | 11 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 14 | START | 14 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 14 | START | 27 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 14 | START | 14 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 14 | START | 14 | 48 |
| ✅ EXACT | `Action_PassBlock` | RT | `21` | `21` | 14 | START | 14 | 210 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `2` | `2` | 26 | START | 26 | 92 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 26 | END | 11 | 26 |
| ✅ EXACT | `Action_ThrowPass` | QB | `6` | `6` | 64 | START | 64 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `2` | `2` | 93 | START | 93 | 179 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 26 | 16 | inferred_complete_timeline |
| `Action_None` | 27 | 63 | 37 | inferred_complete_timeline |
| `Action_ThrowPass` | 64 | 76 | 13 | inferred_complete_timeline |
| `Action_None` | 77 | 210 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 62 | 52 | inferred_complete_timeline |
| `Action_None` | 66 | 210 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 26 | 92 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 93 | 179 | 87 | inferred_complete_timeline |
| `Action_BallCarry` | 185 | 203 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 48 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 57 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 181 | 168 | inferred_complete_timeline |
| `Action_PassBlock` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 26 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 57 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 130 | 69 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 210 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 53 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 59 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 185 | 175 | inferred_complete_timeline |
| `Action_None` | 187 | 197 | 11 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 201 | 191 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 55 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 169 | 159 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 58–59 | 2 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 64–99 | 36 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 69–210 | 142 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 82–88 | 6 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 84–85 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 88–210 | 123 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 98–105 | 7 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 98–210 | 98 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 103–105 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 115–210 | 50 | 8 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 143–146 | 4 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 148–205 | 19 | 4 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 153–158 | 6 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [11–26], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=27.
- ⚠️ Action 'Action_None' range [11-55] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [93-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-203] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-62] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-185] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-197] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [194-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-130] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-53] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-137] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>