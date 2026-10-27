# Play-Annotation-Generator Annotation Review — Counter_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_69`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `7` | `6` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 27 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 25 | START | 25 | 42 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `12` | `11` | 28 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `18` | `17` | 28 | START | 28 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 28 | START | 28 | 45 |
| ✅ EXACT | `Action_PullBlock` | LG | `22` | `21` | 28 | START | 28 | 63 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `7` | `6` | 28 | START | 28 | 102 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `17` | `16` | 31 | START | 31 | 77 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 42 | END | 25 | 42 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 55 | START | 55 | 77 |
| ✅ EXACT | `Action_BallCarry` | RB | `17` | `16` | 78 | START | 78 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 102 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 42 | 18 | inferred_complete_timeline |
| `Action_None` | 43 | 54 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 55 | 77 | 23 | inferred_complete_timeline |
| `Action_None` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_None` | 89 | 95 | 7 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 31 | 77 | 47 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 239 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 28 | 102 | 75 | inferred_complete_timeline |
| `Action_None` | 103 | 239 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 63 | 39 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_None` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 80 | 239 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PullBlock` | 28 | 63 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 42 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 28 | 45 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 59 | 64 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 67 | 69 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 28 | 77 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 102 | 23 | inferred_complete_timeline |
| `Action_None` | 103 | 239 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 111 | 87 | inferred_complete_timeline |
| `Action_None` | 115 | 204 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 90 | 66 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 99 | 75 | inferred_complete_timeline |
| `Action_None` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 74 | 50 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 93 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 213 | 189 | inferred_complete_timeline |
| `Action_None` | 218 | 232 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 123 | 99 | inferred_complete_timeline |
| `Action_None` | 125 | 176 | 52 | inferred_complete_timeline |
| `Action_None` | 180 | 218 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 71–171 | 100 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 76–239 | 162 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 78–107 | 30 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 96–221 | 116 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 98–101 | 4 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 100–146 | 44 | 3 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 117–175 | 51 | 2 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 136–181 | 46 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 145–208 | 41 | 6 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 168–239 | 72 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 225–239 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `12` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [25–42], lower_priority='Action_DownBlock' annotated_start=28, effective_Action_DownBlock_start=43.
- ⚠️ Action 'Action_None' range [25-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-74] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-99] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [25-42] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-93] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-218] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [28-77] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [28-45] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [49-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [59-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [67-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [28-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-107] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-130] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-175] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-181] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-171] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '32' has 1 frames without a visible bounding box.
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