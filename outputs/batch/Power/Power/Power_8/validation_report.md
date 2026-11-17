# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_8`
- **Input XML**: `outputs/batch/Power/Power/Power_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 55 |
| Player Tracks | 55 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Overlapping action conflict at frame 107 for track '4': 'Action_DownBlock' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
> - Action 'Action_PreSnap' range [31-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-173] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-234] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-167] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-208] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [107-121] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-159] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-163] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-165] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-161] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-151] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-156] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-198] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-240] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-244] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-279] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-285] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-291] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-161] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-165] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-195] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-201] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-275] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-174] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-299] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-255] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-217] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-201] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-253] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-230] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-238] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-252] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-246] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-256] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-253] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-275] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-252] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-253] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-255] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-279] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-267] for track '52' has 2 frames without a visible bounding box.
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
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.