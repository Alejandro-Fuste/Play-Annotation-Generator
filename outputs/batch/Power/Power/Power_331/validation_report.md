# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_331`
- **Input XML**: `outputs/batch/Power/Power/Power_331/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '6' (LG) duration 100 frames exceeds threshold 90 frames [start=135, end=234].
> - Validation warning: Action 'Action_DownBlock' for track '14' (RG) duration 100 frames exceeds threshold 90 frames [start=135, end=234].
> - Validation warning: Action 'Action_DownBlock' for track '19' (RT) duration 100 frames exceeds threshold 90 frames [start=135, end=234].
> - Action 'Action_PreSnap' range [0-216] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-284] for track '1' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-290] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-294] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-293] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [135-234] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-264] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-214] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-224] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-240] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-296] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-282] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' for track '13' starts at frame 135, but the player has no visible bounding box on this frame.
> - Action 'Action_DownBlock' range [135-140] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [143-147] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [208-224] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-245] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-299] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-281] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-234] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-257] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-267] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-240] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-299] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-246] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-255] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-256] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-299] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-299] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-299] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.