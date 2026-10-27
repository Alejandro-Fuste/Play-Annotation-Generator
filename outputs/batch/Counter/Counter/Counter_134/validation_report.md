# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_134`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_134/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 111 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 463 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 270: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 463 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [200–212], lower_priority='Action_DownBlock' annotated_start=204, effective_Action_DownBlock_start=213.
> - Action 'Action_None' range [200-258] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-455] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-463] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-290] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-315] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-366] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [375-376] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-310] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-391] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-259] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [204-218] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-263] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-349] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [355-366] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-377] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-387] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-407] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-410] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-447] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-237] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [213-254] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [259-266] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-368] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [204-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [260-290] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-233] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-259] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-313] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-140] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 200, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [200-202] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-272] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-246] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-260] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-319] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-463] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-346] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-340] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-351] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-463] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-310] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-334] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-395] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-463] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-351] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-430] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-305] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-349] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-350] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-372] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-385] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-398] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-425] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-445] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-432] for track '32' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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