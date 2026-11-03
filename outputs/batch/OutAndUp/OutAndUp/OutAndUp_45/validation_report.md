# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_45`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 134 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [27–31], lower_priority='Action_PassBlock' annotated_start=31, effective_Action_PassBlock_start=32.
> - Action 'Action_None' range [27-135] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-145] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-44] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-125] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-269] for track '4' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '5' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-156] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-258] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-267] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-102] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [118-158] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-233] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-158] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-47] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-125] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [141-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [208-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-221] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-256] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [102-156] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [158-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-156] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-241] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-256] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-70] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [117-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [130-133] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [136-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [141-153] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-133] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-160] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [106-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [129-269] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [123-134] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '21' starts at frame 31, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [31-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [33-102] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [108-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [129-134] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [141-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [153-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [159-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [223-228] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-145] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-156] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-170] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-190] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-269] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-153] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-197] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-205] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-223] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-215] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-222] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-255] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-259] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-267] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-256] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-265] for track '31' has 1 frames without a visible bounding box.
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