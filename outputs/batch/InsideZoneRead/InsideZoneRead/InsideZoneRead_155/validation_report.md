# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_155`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_155/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 30 |
| Ball Tracks | 3 |
| CSV events parsed | 18 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [64–77], lower_priority='Action_ZoneBlock' annotated_start=67, effective_Action_ZoneBlock_start=78.
> - Action 'Action_PreSnap' range [0-12] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-36] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-172] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-259] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-122] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [79-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [129-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [201-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-107] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-219] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-69] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-181] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-10] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-25] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-63] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-133] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 118, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [118-154] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-264] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-193] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [99-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-125] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-211] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-261] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-261] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '31' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.