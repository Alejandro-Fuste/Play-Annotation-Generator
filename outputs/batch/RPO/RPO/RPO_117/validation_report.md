# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_117`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_117/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 116 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_RunBlock' for track '15' has invalid range: start=74, end=65. Clamping end to start.
> - Action 'Action_None' range [73-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-129] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-107] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-161] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-189] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-239] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-164] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-164] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-186] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-90] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-132] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-162] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [80-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [101-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-212] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 73, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [73-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [114-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [125-132] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [77-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [116-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [115-128] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-25] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-35] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-43] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-62] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '21' starts at frame 73, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [73-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-239] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [120-128] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-174] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-237] for track '26' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [180-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-205] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-199] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-238] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-239] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-239] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-220] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-208] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-215] for track '36' has 1 frames without a visible bounding box.
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