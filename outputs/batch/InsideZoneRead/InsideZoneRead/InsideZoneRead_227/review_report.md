# Play-Annotation-Generator Annotation Review — InsideZoneRead_227

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_227`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 5
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | LB2 | defense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | LB2 | defense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_Handoff` | LB2 | defense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | CB4 | defense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 7 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 7 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 7 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 7 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 7 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 7 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 7 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 7 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 7 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 7 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 7 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | QB | `14` | `13` | 85 | START | 85 | 101 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `19` | `18` | 88 | START | 89 | 150 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `19` | `18` | 88 | START | 89 | 150 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LT | `21` | `20` | 88 | START | 90 | 93 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `22` | `21` | 88 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `8` | `7` | 88 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | LB2 | `11` | `10` | 101 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | LB2 | `11` | `10` | 103 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Handoff` | LB2 | `11` | `10` | 116 | START | N/A | N/A |
| ✅ EXACT | `Action_BallCarry` | CB4 | `9` | `8` | 123 | START | 123 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 158 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 84 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 85 | 101 | 17 | inferred_complete_timeline |
| `Action_None` | 102 | 150 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 150 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 92 | 8 | inferred_complete_timeline |
| `Action_None` | 96 | 150 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 147 | 63 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 139 | 55 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 34 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 50 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 66 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 93 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 66 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 60 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 60 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 65 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 150 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 66 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–23
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 64 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 66 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 76 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 80 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 150 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 84 | 5 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 108 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 150 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 122 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 150 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 93 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 4–41 | 25 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 10–13 | 4 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 46–65 | 20 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 85–90 | 6 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 101–150 | 41 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 118–150 | 33 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 125–150 | 26 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 125–145 | 18 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 130–150 | 21 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 134–144 | 8 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 138–145 | 8 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 142–147 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `19` (RG): Annotated start 88 != Inferred start 89
- ⚠️ `Action_ZoneBlock` for actor_track_id `19` (RG): Annotated start 88 != Inferred start 89
- ⚠️ `Action_ZoneBlock` for actor_track_id `21` (LT): Annotated start 88 != Inferred start 90
- ❌ Missing segment for action `Action_ZoneBlock` on target `22` (LG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `8` (RT)
- ❌ Missing segment for action `Action_SnapReceive` on target `11` (LB2)
- ❌ Missing segment for action `Action_ReadDefender` on target `11` (LB2)
- ❌ Missing segment for action `Action_Handoff` on target `11` (LB2)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 6 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '7' has invalid range: start=88, end=66. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '10' has invalid range: start=85, end=80. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '10' has invalid range: start=103, end=80. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '10' has invalid range: start=116, end=80. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '17' has invalid range: start=88, end=60. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=88, end=69. Clamping end to start.
- ⚠️ Action 'Action_None' range [85-147] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-64] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-76] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-60] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-150] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-93] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-66] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-14] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-25] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-41] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-13] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-65] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-90] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-118] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-145] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_227'; source metadata written as null.

</details>