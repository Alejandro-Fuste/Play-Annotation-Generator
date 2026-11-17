# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_102`
- **Input XML**: `outputs/batch/Power/Power/Power_102/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [5-202] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-255] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-169] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-213] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-259] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-201] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [137-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-285] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-300] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-308] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [137-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [161-165] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [137-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [146-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [180-181] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-214] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-265] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-181] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-285] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-186] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-214] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-246] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-272] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-247] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' for track '14' starts at frame 137, but the player has no visible bounding box on this frame.
> - Action 'Action_DownBlock' range [137-176] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [192-236] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [243-252] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-236] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-247] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-197] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-224] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-194] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-194] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-202] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-275] for track '22' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.