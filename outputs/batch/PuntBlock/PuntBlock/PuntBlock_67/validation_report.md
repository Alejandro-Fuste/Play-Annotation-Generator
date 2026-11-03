# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_67`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 58 |
| Player Tracks | 58 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 166 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [1-237] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-196] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-219] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [53-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [97-223] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-19] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-169] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-269] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-44] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-217] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [65-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-269] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [1-47] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-26] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-111] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-121] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-132] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-123] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-145] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-185] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-215] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-269] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-165] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-16] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' for track '19' starts at frame 1, but the player has no visible bounding box on this frame.
> - Action 'Action_LongSnap' range [1-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [6-52] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 53, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [53-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-164] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-19] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-185] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [189-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-229] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [46-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-68] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-171] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-108] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-131] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-242] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [115-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-190] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-203] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-217] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-156] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-189] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-204] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-218] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-167] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [171-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-143] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-155] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-183] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-215] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-192] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-208] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-224] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-269] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-269] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-256] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-269] for track '49' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-256] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-266] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-265] for track '57' has 1 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.