# Play-Annotation-Generator Annotation Review — Counter_311

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_311`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB1 | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB1 | offense | `12` | `11` |
| ✅ EXACT | `Action_BallSnap` | QB1 | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `12` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 3 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_DownBlock` | C | `18` | `17` | 32 | START | 32 | 86 |
| ✅ EXACT | `Action_DownBlock` | LT | `21` | `20` | 32 | START | 32 | 86 |
| ✅ EXACT | `Action_DownBlock` | LT | `21` | `20` | 32 | START | 32 | 86 |
| ✅ EXACT | `Action_PullBlock` | RG | `11` | `10` | 32 | START | 32 | 36 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `1` | `0` | 32 | START | 32 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `10` | `9` | 34 | START | 34 | 52 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB1 | `12` | `11` | 38 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB1 | `12` | `11` | 56 | START | 56 | 57 |
| ✅ EXACT | `Action_BallSnap` | QB1 | `12` | `11` | 58 | START | 58 | 58 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `10` | `9` | 74 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 86 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_Handoff` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 59 | 73 | 15 | inferred_complete_timeline |
| `Action_None` | 74 | 150 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 34 | 52 | 19 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 55 | 56 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 134 | 77 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 32 | 86 | 55 | inferred_complete_timeline |
| `Action_None` | 87 | 150 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 31 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 32 | 86 | 55 | inferred_complete_timeline |
| `Action_None` | 87 | 150 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–2
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 32 | 86 | 55 | inferred_complete_timeline |
| `Action_None` | 87 | 150 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PullBlock` | 32 | 36 | 5 | inferred_complete_timeline |
| `Action_None` | 97 | 150 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 105 | 119 | 15 | inferred_complete_timeline |
| `Action_None` | 124 | 150 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 130 | 73 | inferred_complete_timeline |
| `Action_None` | 134 | 144 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 57 | 48 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 40 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 50 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 57 | 6 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 57 | 13 | inferred_complete_timeline |
| `Action_None` | 58 | 70 | 13 | inferred_complete_timeline |
| `Action_None` | 81 | 150 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 57 | 34 | inferred_complete_timeline |
| `Action_None` | 58 | 79 | 22 | inferred_complete_timeline |
| `Action_None` | 86 | 101 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 10–97 | 80 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 25–26 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 39–150 | 111 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 48–150 | 103 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 49–121 | 67 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 60–150 | 86 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 135–150 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `12` (QB1)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `12` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `10` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '9' has invalid range: start=74, end=56. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '11' has invalid range: start=58, end=38. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '11' has invalid range: start=58, end=38. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '19' has invalid range: start=32, end=2. Clamping end to start.
- ⚠️ Action 'Action_None' range [87-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-134] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [34-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [55-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [32-36] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-40] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-70] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-57] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-101] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-71] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-83] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-57] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-54] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-81] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>