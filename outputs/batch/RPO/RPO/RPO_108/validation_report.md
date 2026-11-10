# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_108`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_108/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 54 |
| Player Tracks | 54 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 133 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [34-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-134] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-264] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-228] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-118] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-80] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-95] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-109] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-116] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-172] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-117] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-106] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-60] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-89] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [62-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-198] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-104] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-67] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-117] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-224] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-106] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-151] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-269] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-160] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-221] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-186] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-177] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-174] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-149] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-201] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-201] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-178] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-216] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-209] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-233] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-264] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-262] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-264] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-269] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-268] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '51' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.