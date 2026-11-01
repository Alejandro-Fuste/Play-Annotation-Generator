# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_362`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_362/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '6' has invalid range: start=61, end=51. Clamping end to start.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [16–30], lower_priority='Action_ZoneBlock' annotated_start=19, effective_Action_ZoneBlock_start=31.
> - Action 'Action_None' range [16-239] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-163] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-57] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-43] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-62] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-88] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-95] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [16-26] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [42-51] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-42] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-27] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-78] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-32] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-218] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-47] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-155] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [168-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-37] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-10] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-219] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-28] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-48] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-34] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-54] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-73] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-95] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-117] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-151] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-66] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-97] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-163] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-215] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-89] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [97-108] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-127] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-141] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-236] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-134] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-141] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-170] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-141] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [113-201] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-221] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-237] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-239] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '34' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.