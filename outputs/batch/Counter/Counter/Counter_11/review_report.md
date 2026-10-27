# Play-Annotation-Generator Annotation Review — Counter_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_11`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `17` | `16` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 3 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 3 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 3 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 3 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 3 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 3 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 3 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 3 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 3 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 3 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 3 | START | 0 | 82 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 77 | START | 77 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `14` | `13` | 83 | START | 83 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `22` | `21` | 83 | START | 97 | 116 |
| ✅ EXACT | `Action_DownBlock` | RT | `9` | `8` | 83 | START | 83 | 99 |
| ✅ EXACT | `Action_PullBlock` | LG | `17` | `16` | 83 | START | 83 | 172 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `7` | `6` | 83 | START | 83 | 172 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `18` | 96 | START | 96 | 118 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `19` | `18` | 96 | END | N/A | N/A |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 119 | START | 119 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 172 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_Handoff` | 96 | 118 | 23 | inferred_complete_timeline |
| `Action_None` | 119 | 299 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_BallCarry` | 119 | 299 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 299 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 299 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 192 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 122 | 46 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 142 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 83 | 172 | 90 | inferred_complete_timeline |
| `Action_None` | 173 | 299 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PullBlock` | 83 | 172 | 90 | inferred_complete_timeline |
| `Action_None` | 173 | 299 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 96 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 116 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 172 | 49 | inferred_complete_timeline |
| `Action_None` | 173 | 299 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_DownBlock` | 83 | 101 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 130 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 141 | 152 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 165 | 172 | 8 | inferred_complete_timeline |
| `Action_None` | 173 | 258 | 86 | inferred_complete_timeline |
| `Action_None` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_DownBlock` | 83 | 99 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 161 | 85 | inferred_complete_timeline |
| `Action_None` | 163 | 289 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 121 | 45 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 103 | 27 | inferred_complete_timeline |
| `Action_None` | 108 | 140 | 33 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |
| `Action_None` | 148 | 155 | 8 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 264 | 102 | inferred_complete_timeline |
| `Action_None` | 273 | 283 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 129 | 53 | inferred_complete_timeline |
| `Action_None` | 134 | 299 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 299 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 246 | 170 | inferred_complete_timeline |
| `Action_None` | 249 | 299 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 299 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 224 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 299 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 299 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 299 | 223 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 117–299 | 177 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 163–170 | 8 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 179–299 | 121 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 191–299 | 92 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 196–248 | 28 | 6 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 206–299 | 32 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 212–299 | 82 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 242–299 | 58 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `19` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 96 for track '18': 'Action_SnapReceive' vs 'Action_Handoff'. Overriding with 'Action_Handoff'.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [77–96], lower_priority='Action_DownBlock' annotated_start=83, effective_Action_DownBlock_start=97.
- ⚠️ Action 'Action_None' range [77-224] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-246] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-289] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [83-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-103] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-140] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-264] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-283] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [83-101] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [141-152] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-129] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-122] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-142] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-271] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-299] for track '31' has 1 frames without a visible bounding box.
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