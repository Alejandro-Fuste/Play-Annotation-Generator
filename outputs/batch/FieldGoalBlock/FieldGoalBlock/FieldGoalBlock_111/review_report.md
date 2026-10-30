# Play-Annotation-Generator Annotation Review — FieldGoalBlock_111

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_111`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 106
- **Ball Tracks:** 0
- **Action Segments:** 292
- **Validation Warnings:** 458
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 279
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `6` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `4` | `4` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `4` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `5` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `6` | `Group` | 0 | START | 0 | 38 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `4` | `4` | 17 | START | 17 | 26 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 39 | START | 39 | 44 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PlaceBall` | 17 | 26 | 10 | inferred_complete_timeline |
| `Action_None` | 27 | 79 | 53 | inferred_complete_timeline |
| `Action_None` | 81 | 96 | 16 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_KickBall` | 39 | 44 | 6 | inferred_complete_timeline |
| `Action_None` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_None` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 59 | 77 | 19 | inferred_complete_timeline |
| `Action_None` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 39 | 44 | 6 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_None` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_None` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 50 | 12 | inferred_complete_timeline |
| `Action_None` | 101 | 104 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 38 | 30 | inferred_complete_timeline |
| `Action_None` | 39 | 94 | 56 | inferred_complete_timeline |
| `Action_None` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_None` | 126 | 233 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_None` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 96 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 104 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 96 | 58 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 52 | 14 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_None` | 106 | 110 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 37 | 6 | inferred_complete_timeline |
| `Action_None` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_None` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 50 | 53 | 4 | inferred_complete_timeline |
| `Action_None` | 58 | 65 | 8 | inferred_complete_timeline |
| `Action_None` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_None` | 75 | 101 | 27 | inferred_complete_timeline |
| `Action_None` | 104 | 110 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_None` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_None` | 48 | 57 | 10 | inferred_complete_timeline |
| `Action_None` | 60 | 96 | 37 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_None` | 39 | 96 | 58 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 96 | 58 | inferred_complete_timeline |
| `Action_None` | 104 | 110 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 24 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 38 | 13 | inferred_complete_timeline |
| `Action_None` | 39 | 58 | 20 | inferred_complete_timeline |
| `Action_None` | 144 | 171 | 28 | inferred_complete_timeline |
| `Action_None` | 174 | 329 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 96 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 59 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 6–103 | 52 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 7–291 | 137 | 8 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 34–112 | 50 | 6 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 42–58 | 17 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 43–329 | 168 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 59–101 | 10 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 61–104 | 13 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 61–175 | 40 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 61–116 | 41 | 6 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 63–109 | 42 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 73–110 | 34 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 79–96 | 18 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 80–96 | 17 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 80–329 | 193 | 7 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 82–288 | 178 | 7 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 82–118 | 10 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 86–103 | 15 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 92–96 | 5 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 97–98 | 2 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 97–116 | 10 | 3 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 97–98 | 2 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 97–98 | 2 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 97–129 | 30 | 3 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 97–329 | 179 | 10 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 97–101 | 5 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 97–289 | 143 | 6 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 97–104 | 6 | 2 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 99–101 | 3 | 1 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 99–120 | 12 | 2 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 99–101 | 3 | 1 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 99–101 | 3 | 1 | Undefined position; Undefined team |
| `47` | `58` | Position_Unknown | Team_Unknown | 99–125 | 11 | 3 | Undefined position; Undefined team |
| `48` | `59` | Position_Unknown | Team_Unknown | 99–104 | 5 | 2 | Undefined position; Undefined team |
| `49` | `60` | Position_Unknown | Team_Unknown | 99–210 | 108 | 4 | Undefined position; Undefined team |
| `50` | `61` | Position_Unknown | Team_Unknown | 99–329 | 138 | 5 | Undefined position; Undefined team |
| `51` | `63` | Position_Unknown | Team_Unknown | 102–104 | 3 | 1 | Undefined position; Undefined team |
| `52` | `65` | Position_Unknown | Team_Unknown | 102–108 | 5 | 2 | Undefined position; Undefined team |
| `53` | `66` | Position_Unknown | Team_Unknown | 102–106 | 5 | 1 | Undefined position; Undefined team |
| `54` | `67` | Position_Unknown | Team_Unknown | 102–104 | 3 | 1 | Undefined position; Undefined team |
| `55` | `68` | Position_Unknown | Team_Unknown | 102–118 | 13 | 4 | Undefined position; Undefined team |
| `56` | `69` | Position_Unknown | Team_Unknown | 102–110 | 6 | 2 | Undefined position; Undefined team |
| `57` | `71` | Position_Unknown | Team_Unknown | 105–110 | 6 | 1 | Undefined position; Undefined team |
| `58` | `72` | Position_Unknown | Team_Unknown | 105–174 | 36 | 4 | Undefined position; Undefined team |
| `59` | `73` | Position_Unknown | Team_Unknown | 105–110 | 6 | 1 | Undefined position; Undefined team |
| `60` | `74` | Position_Unknown | Team_Unknown | 105–118 | 13 | 2 | Undefined position; Undefined team |
| `61` | `75` | Position_Unknown | Team_Unknown | 105–108 | 4 | 1 | Undefined position; Undefined team |
| `62` | `76` | Position_Unknown | Team_Unknown | 105–110 | 6 | 1 | Undefined position; Undefined team |
| `63` | `77` | Position_Unknown | Team_Unknown | 105–329 | 222 | 2 | Undefined position; Undefined team |
| `64` | `78` | Position_Unknown | Team_Unknown | 105–125 | 20 | 2 | Undefined position; Undefined team |
| `65` | `80` | Position_Unknown | Team_Unknown | 107–109 | 3 | 1 | Undefined position; Undefined team |
| `66` | `82` | Position_Unknown | Team_Unknown | 108–112 | 5 | 1 | Undefined position; Undefined team |
| `67` | `83` | Position_Unknown | Team_Unknown | 111–126 | 13 | 2 | Undefined position; Undefined team |
| `68` | `84` | Position_Unknown | Team_Unknown | 111–115 | 5 | 1 | Undefined position; Undefined team |
| `69` | `85` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `70` | `86` | Position_Unknown | Team_Unknown | 111–122 | 12 | 1 | Undefined position; Undefined team |
| `71` | `87` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `72` | `88` | Position_Unknown | Team_Unknown | 111–291 | 136 | 4 | Undefined position; Undefined team |
| `73` | `89` | Position_Unknown | Team_Unknown | 111–134 | 19 | 2 | Undefined position; Undefined team |
| `74` | `90` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `75` | `91` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `76` | `92` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `77` | `93` | Position_Unknown | Team_Unknown | 113–115 | 3 | 1 | Undefined position; Undefined team |
| `78` | `94` | Position_Unknown | Team_Unknown | 113–132 | 20 | 1 | Undefined position; Undefined team |
| `79` | `95` | Position_Unknown | Team_Unknown | 113–146 | 34 | 1 | Undefined position; Undefined team |
| `80` | `96` | Position_Unknown | Team_Unknown | 113–237 | 50 | 7 | Undefined position; Undefined team |
| `81` | `97` | Position_Unknown | Team_Unknown | 113–290 | 167 | 3 | Undefined position; Undefined team |
| `82` | `100` | Position_Unknown | Team_Unknown | 117–118 | 2 | 1 | Undefined position; Undefined team |
| `83` | `101` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `84` | `102` | Position_Unknown | Team_Unknown | 121–122 | 2 | 1 | Undefined position; Undefined team |
| `85` | `104` | Position_Unknown | Team_Unknown | 160–184 | 25 | 1 | Undefined position; Undefined team |
| `86` | `105` | Position_Unknown | Team_Unknown | 165–325 | 148 | 4 | Undefined position; Undefined team |
| `87` | `107` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |
| `88` | `108` | Position_Unknown | Team_Unknown | 172–329 | 156 | 3 | Undefined position; Undefined team |
| `89` | `110` | Position_Unknown | Team_Unknown | 182–329 | 145 | 4 | Undefined position; Undefined team |
| `90` | `111` | Position_Unknown | Team_Unknown | 183–221 | 29 | 3 | Undefined position; Undefined team |
| `91` | `113` | Position_Unknown | Team_Unknown | 188–328 | 132 | 3 | Undefined position; Undefined team |
| `92` | `114` | Position_Unknown | Team_Unknown | 191–329 | 139 | 1 | Undefined position; Undefined team |
| `93` | `115` | Position_Unknown | Team_Unknown | 197–329 | 133 | 1 | Undefined position; Undefined team |
| `94` | `116` | Position_Unknown | Team_Unknown | 199–203 | 5 | 1 | Undefined position; Undefined team |
| `95` | `117` | Position_Unknown | Team_Unknown | 224–227 | 4 | 1 | Undefined position; Undefined team |
| `96` | `118` | Position_Unknown | Team_Unknown | 228–329 | 102 | 1 | Undefined position; Undefined team |
| `97` | `119` | Position_Unknown | Team_Unknown | 231–329 | 99 | 1 | Undefined position; Undefined team |
| `98` | `120` | Position_Unknown | Team_Unknown | 239–285 | 47 | 1 | Undefined position; Undefined team |
| `99` | `121` | Position_Unknown | Team_Unknown | 251–305 | 26 | 4 | Undefined position; Undefined team |
| `100` | `122` | Position_Unknown | Team_Unknown | 258–261 | 4 | 1 | Undefined position; Undefined team |
| `101` | `124` | Position_Unknown | Team_Unknown | 268–329 | 58 | 4 | Undefined position; Undefined team |
| `102` | `125` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `103` | `128` | Position_Unknown | Team_Unknown | 295–297 | 3 | 1 | Undefined position; Undefined team |
| `104` | `129` | Position_Unknown | Team_Unknown | 326–328 | 3 | 1 | Undefined position; Undefined team |
| `105` | `130` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ 90 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 90 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BlockKick' at frame 44 targets track ID '-', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 180 |
| Missing visible bounding boxes during action | 277 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [39-96] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 45, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [45-45] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-55] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-77] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-59] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-96] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-50] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-18] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-24] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-38] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-58] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 39, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [39-39] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-57] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-96] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-52] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-27] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-28] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-101] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-38] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-94] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-233] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-44] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-38] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-19] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-81] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-287] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-110] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-101] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-78] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-104] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-79] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-91] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-109] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-95] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-96] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-96] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-98] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-96] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-239] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-274] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-98] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-126] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-146] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-186] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-214] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-269] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-305] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-329] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-135] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-186] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-257] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-197] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-182] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-240] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-287] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-329] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-157] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-112] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-329] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-125] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-126] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-122] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-280] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-134] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-132] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-146] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '80' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-208] for track '80' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-274] for track '81' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-184] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-195] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '86' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-291] for track '86' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-325] for track '86' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-186] for track '88' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-244] for track '88' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-212] for track '90' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-204] for track '91' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-312] for track '91' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-328] for track '91' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-329] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-285] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-262] for track '99' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-305] for track '99' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-277] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-329] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '102' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '92' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '92' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '93' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '93' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '94' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '94' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '95' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '95' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '96' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '96' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '97' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '97' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '98' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '98' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '99' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '99' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '100' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '100' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '101' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '101' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '102' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '102' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '103' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '103' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '104' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '104' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '105' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '105' has undefined team_side. Will map to Team_Unknown.

</details>