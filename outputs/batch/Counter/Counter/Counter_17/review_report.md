# Play-Annotation-Generator Annotation Review — Counter_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_17`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | CB2 | defense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `12` | `11` | 62 | START | 62 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `18` | `17` | 62 | START | 62 | 97 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `21` | `20` | 62 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `22` | `21` | 62 | START | 62 | 84 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 64 | START | 64 | 77 |
| ✅ EXACT | `Action_PullLeadBlock` | CB2 | `7` | `6` | 67 | START | 67 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `14` | `13` | 70 | START | 70 | 111 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 78 | END | 64 | 78 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 91 | START | 91 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `4` | `3` | 100 | START | 100 | 141 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 144 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_None` | 100 | 117 | 18 | inferred_complete_timeline |
| `Action_None` | 121 | 210 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 70 | 111 | 42 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 113 | 132 | 20 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 137 | 145 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 204 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 141 | 42 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 210 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 124 | 61 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 157 | 13 | inferred_complete_timeline |
| `Action_None` | 168 | 181 | 14 | inferred_complete_timeline |
| `Action_None` | 183 | 210 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullBlock` | 62 | 84 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 100 | 106 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 64 | 77 | 14 | inferred_complete_timeline |
| `Action_None` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 121 | 23 | inferred_complete_timeline |
| `Action_None` | 127 | 210 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 81 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 92 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 97 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 121 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 94 | 31 | inferred_complete_timeline |
| `Action_None` | 96 | 210 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 85 | 22 | inferred_complete_timeline |
| `Action_None` | 90 | 111 | 22 | inferred_complete_timeline |
| `Action_None` | 113 | 210 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 85 | 22 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 112 | 49 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 127 | 210 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 121 | 58 | inferred_complete_timeline |
| `Action_None` | 127 | 148 | 22 | inferred_complete_timeline |
| `Action_None` | 150 | 163 | 14 | inferred_complete_timeline |
| `Action_None` | 185 | 210 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 122 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 67 | 144 | 78 | inferred_complete_timeline |
| `Action_None` | 145 | 210 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 164 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 113–210 | 98 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 117–210 | 52 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 148–210 | 52 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 172–210 | 26 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 177–180 | 4 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 184–210 | 23 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `21` (C)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [64–78], lower_priority='Action_DownBlock' annotated_start=62, effective_Action_DownBlock_start=79.
- ⚠️ Action 'Action_None' range [64-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-164] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-81] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-112] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [70-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [113-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [137-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-124] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-157] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-181] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [64-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [62-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [90-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [100-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-192] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '28' has 1 frames without a visible bounding box.
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

</details>