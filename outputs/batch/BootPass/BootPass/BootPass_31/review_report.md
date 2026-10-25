# Play-Annotation-Generator Annotation Review — BootPass_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_31`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 10
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_RunFlatRoute` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_SecureCatch` | TE | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 16 | START | 16 | 40 |
| ✅ EXACT | `Action_RunBlock` | LT | `12` | `12` | 27 | START | 27 | 210 |
| ✅ EXACT | `Action_RunBlock` | RG | `15` | `15` | 27 | START | 27 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `20` | `20` | 27 | START | 47 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `21` | `21` | 27 | START | 27 | 94 |
| ✅ EXACT | `Action_RunBlock` | RT | `4` | `4` | 27 | START | 27 | 210 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 40 | END | 16 | 40 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `9` | `9` | 49 | START | 49 | 68 |
| ✅ EXACT | `Action_BootAway` | QB | `9` | `9` | 73 | START | 73 | 84 |
| ✅ EXACT | `Action_RunFlatRoute` | TE | `3` | `3` | 75 | START | 75 | 106 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 85 | START | 85 | 97 |
| ✅ EXACT | `Action_SecureCatch` | TE | `3` | `3` | 108 | START | 108 | 118 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_None` | 41 | 48 | 8 | inferred_complete_timeline |
| `Action_FakeHandoff` | 49 | 68 | 20 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_BootAway` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 85 | 97 | 13 | inferred_complete_timeline |
| `Action_None` | 98 | 210 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 53 | 38 | inferred_complete_timeline |
| `Action_None` | 58 | 210 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 75 | 106 | 32 | inferred_complete_timeline |
| `Action_None` | 107 | 107 | 1 | inferred_complete_timeline |
| `Action_SecureCatch` | 108 | 118 | 11 | inferred_complete_timeline |
| `Action_None` | 119 | 210 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunBlock` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunBlock` | 27 | 94 | 68 | inferred_complete_timeline |
| `Action_RunBlock` | 98 | 110 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 55 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunBlock` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunBlock` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 39 | 24 | inferred_complete_timeline |
| `Action_None` | 45 | 70 | 26 | inferred_complete_timeline |
| `Action_None` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_None` | 91 | 210 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 194 | 179 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 80 | 65 | inferred_complete_timeline |
| `Action_None` | 85 | 182 | 98 | inferred_complete_timeline |
| `Action_None` | 185 | 192 | 8 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 200 | 185 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 103 | 88 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 86 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 86 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–83 | 79 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 3–107 | 21 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 67–210 | 144 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 87–210 | 124 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 87–185 | 99 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 89–120 | 31 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 91–200 | 87 | 8 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 96–103 | 8 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 104–210 | 102 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 106–210 | 105 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 113–118 | 6 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 148–185 | 21 | 4 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 182–200 | 11 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 194–210 | 14 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 196–206 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 54: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [16–40], lower_priority='Action_RunBlock' annotated_start=27, effective_Action_RunBlock_start=41.
- ⚠️ Action 'Action_None' range [16-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [27-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-182] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [27-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [27-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-103] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [16-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [57-62] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [64-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [27-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [98-110] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-20] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-210] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-185] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-105] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-120] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>