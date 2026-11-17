# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_53`
- **Input XML**: `outputs/batch/Power/Power/Power_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [26-290] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-226] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-241] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-257] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-284] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-174] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-270] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-274] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-297] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-217] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-247] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-270] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-229] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-235] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-247] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-197] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-297] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-247] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-261] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-276] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-256] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '31' has 1 frames without a visible bounding box.
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