# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_379`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_379/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 128 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_PullBlock' for track '13' has invalid range: start=52, end=48. Clamping end to start.
> - Action 'Action_None' range [49-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-172] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [92-95] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-112] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [116-118] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [194-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-158] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-103] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-53] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-53] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-89] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [52-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [78-89] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [76-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [49-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 49, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [49-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-51] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [52-53] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-16] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-37] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-48] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-89] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-16] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-45] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-162] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-16] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-29] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [82-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-79] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-113] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-136] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-89] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-210] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-165] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '36' has 1 frames without a visible bounding box.
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