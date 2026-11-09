# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_144`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_144/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 33 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [2-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-66] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-261] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-284] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-178] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-229] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-22] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-230] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-260] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-293] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-201] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-261] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-283] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-234] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-243] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-258] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-283] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-17] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-205] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-234] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-185] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-287] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-234] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-154] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-43] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-161] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-178] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-194] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-51] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-68] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-174] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-328] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-220] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-321] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-229] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-246] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-258] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-277] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-308] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.