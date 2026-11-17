# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_296`
- **Input XML**: `outputs/batch/Power/Power/Power_296/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [11-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-218] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-166] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-220] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [139-211] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-184] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-329] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-296] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-183] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-307] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-241] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-279] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-235] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-178] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-35] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-296] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-283] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-296] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-243] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-242] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-243] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-271] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-254] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-259] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-266] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-291] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-308] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-318] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.